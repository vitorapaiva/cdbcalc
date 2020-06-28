# Create your views here.

from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from importcdi.models import CDIHistory
from importcdi.views.treatfiledata import TreatFileData

import json


def import_cdi(request):
    try:
        treat_file_data = TreatFileData()
        if request.method == 'POST':
            json_data = json.loads(request.body)
            cdi_data = treat_file_data.get_file_data_from_url(json_data['url'])
            created = CDIHistory.objects.bulk_create(cdi_data, 100)
            result = {
                'status': 'success',
                'data': format(created)
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
            'error': "Unexpected error: " + str(e)
        }
        return JsonResponse(result, status=400)
