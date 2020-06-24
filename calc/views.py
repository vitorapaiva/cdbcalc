# Create your views here.
from django.http import JsonResponse


def calc(request):
    cdbcalc = {
        'calc': 0
    }
    return JsonResponse(cdbcalc)
