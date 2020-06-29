import json
from datetime import datetime, timedelta

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from importcdi.models.cdihistory import CDIHistory


def validate_request_date(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    min_date = CDIHistory.objects.order_by('cdi_date').first().cdi_date
    max_date = CDIHistory.objects.order_by('cdi_date').last().cdi_date
    if start_date > end_date:
        raise Exception('Datas inválidas')
    if start_date.date() < min_date:
        raise Exception('Não há dados disponiveis para essa busca. Data mínima: ' + min_date.strftime('%d/%m/%Y'))
    if end_date.date() > max_date:
        raise Exception('Não há dados disponiveis para essa busca. Data máxima: ' + max_date.strftime('%d/%m/%Y'))


def get_cdi_tax_by_date(start_date, end_date):
    validate_request_date(start_date, end_date)
    return CDIHistory.objects.filter(cdi_date__range=(start_date, end_date)).order_by('cdi_date')


def calculate_accumulated_cdi(cdi_list, invested_amount, cdb_rate):
    cdb_daily = {}
    accumulated_cdi_tax = 1
    if len(cdi_list) == 0:
        raise Exception('Não há dados disponiveis para essa busca')
    cdl_as_list = list(cdi_list)
    cdl_as_list.pop()
    for cdi in cdl_as_list:
        cdi_tax = round(((cdi.cdi_tax_rate / 100 + 1) ** (1 / 252) - 1), 8)
        accumulated_cdi_tax = (1 + cdi_tax * cdb_rate / 100) * accumulated_cdi_tax
        unit_price = invested_amount * round(accumulated_cdi_tax, 16)
        date = cdi.cdi_date.strftime('%Y-%m-%d')
        cdb_daily[date] = {
            'date': date,
            "unitPrice": round(unit_price, 2)
        }
    return cdb_daily


def generate_complete_date_list(start_date, end_date):
    date_list = []

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    diff_days = end_date - start_date

    for minus_day in range(diff_days.days + 1):
        date_list.append((end_date - timedelta(days=minus_day)).strftime('%Y-%m-%d'))

    return date_list


def calc(request):
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            invested_amount = 1000  # default value
            if 'investedAmount' in json_data:
                invested_amount = float(json_data['investedAmount'])

            investment_date = json_data['investmentDate']
            current_date = json_data['currentDate']

            cdb_rate = float(json_data['cdbRate'])

            cdi_list = get_cdi_tax_by_date(investment_date, current_date)
            cdb_daily = calculate_accumulated_cdi(cdi_list, invested_amount, cdb_rate)

            cdb_result = []
            result_index = 0

            date_list = generate_complete_date_list(investment_date, current_date)

            last_date = max(cdb_daily)
            current_amount = cdb_daily[last_date]['unitPrice']

            for date_index in date_list:
                result_cdi = {
                    'date': date_index,
                    "unitPrice": current_amount
                }

                if date_index in cdb_daily.keys():
                    result = cdb_daily[date_index]
                    current_amount = cdb_daily[date_index]["unitPrice"]

                cdb_result.append(result_cdi)
                result_index = result_index + 1

            result = {
                'status': 'success',
                'data': cdb_result
            }

            return JsonResponse(result)
        else:
            raise PermissionDenied('use POST')
    except PermissionDenied as e:
        result = {
            'status': 'failed',
            'error': "Invalid Method: " + str(e)
        }
        return JsonResponse(result, status=400)
    except Exception as e:
        result = {
            'status': 'failed',
            'error': str(e)
        }
        return JsonResponse(result, status=400)
