# Create your views here.
from django.http import JsonResponse


def calc(request):
    taxa_cdi_acumulada = 1
    cdi = 13.88
    taxa_cdi = round(((cdi / 100 + 1) ** (1 / 252) - 1), 8)
    valor_investido = 1000
    taxa_cdb = 103.5
    for x in range(12):
        taxa_cdi_acumulada = taxa_cdi_acumulada + (taxa_cdi * (taxa_cdb / 100))

    cdi = 13.63
    taxa_cdi = round(((cdi / 100 + 1) ** (1 / 252) - 1), 8)
    for x in range(17):
        taxa_cdi_acumulada = taxa_cdi_acumulada + (taxa_cdi * (taxa_cdb / 100))

    taxa_cdi_acumulada = round(taxa_cdi_acumulada, 8)
    print(valor_investido*taxa_cdi_acumulada)
    cdb_result = {
        'date': "2020-06-24",
        "unitPrice": 0
    }
    return JsonResponse(cdb_result)
