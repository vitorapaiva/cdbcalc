# Create your views here.
import codecs
import csv
import datetime
from urllib.request import urlopen

from django.http import JsonResponse

from importcdi.models import CDIHistory


def treatdata(array_data):
    cdi_date = datetime.datetime.strptime(array_data[1], '%d/%m/%Y').strftime('%Y-%m-%d')
    result = CDIHistory(cdi_date=cdi_date, cdi_tax_rate=float(array_data[2]))
    return result


def importcdi(request):
    try:
        file_url = request.url
        url_response = urlopen(file_url)
        file_data = csv.reader(codecs.iterdecode(url_response, 'utf-8'))
        file_rows = list(file_data)
        file_header = file_rows.pop(0)
        cdi_data = *map(treatdata, file_rows),
        CDIHistory.objects.bulk_create(cdi_data)
        result = {
            'status': 'success',
            'data': format(file_rows)
        }
        return JsonResponse(result)
    except Exception as e:
        result = {
            'status': 'false',
            'error': "Unexpected error: " + str(e)
        }
        return JsonResponse(result)
