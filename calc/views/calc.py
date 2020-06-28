import json

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from importcdi.models.cdihistory import CDIHistory


def calc(request):
    try:
        if request.method == 'POST':
            invested_amount = 1000  # default value
            json_data = json.loads(request.body)
            investment_date = json_data['investmentDate']
            current_date = json_data['currentDate']
            if 'investedAmount' in dir(json_data):
                invested_amount = float(json_data['investedAmount'])
            cdb_rate = float(json_data['cdbRate'])

            cdi_list = CDIHistory.objects.filter(cdi_date__range=(investment_date, current_date))

            accumulated_cdi_tax = 1
            dict_index = 0
            cdb_result = {}

            for cdi in cdi_list:
                cdi_tax = round(((cdi.cdi_tax_rate / 100 + 1) ** (1 / 252) - 1), 8)
                accumulated_cdi_tax = accumulated_cdi_tax + (cdi_tax * (cdb_rate / 100))
                accumulated_cdi_tax = round(accumulated_cdi_tax, 8)
                unit_price = invested_amount * accumulated_cdi_tax
                cdb_result[dict_index] = {
                    'date': cdi.cdi_date,
                    "unitPrice": round(unit_price, 2)
                }
                dict_index = dict_index + 1

            return JsonResponse(cdb_result)
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
            'error': "Unexpected error: " + str(e)
        }
        return JsonResponse(result, status=400)
