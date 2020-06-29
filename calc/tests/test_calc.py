from django.test import RequestFactory, TestCase

from calc.views import calc
from importcdi.views import import_cdi


class TestCalc(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_calc_with_no_data(self):
        data = {
            "investmentDate": "2019-11-28",
            "cdbRate": 103.5,
            "currentDate": "2019-12-03"
        }
        request = self.factory.post('api/v1/calc/', data, content_type='application/json')
        response = calc(request)
        self.assertEqual(response.status_code, 400)

    def test_calc_with_import(self):
        data_import = {'url': "http://portalxibe.com.br/CDI_Prices.csv"}
        request_import = self.factory.post('api/v1/cdi/import', data_import, content_type='application/json')
        response_import = import_cdi(request_import)

        self.assertEqual(response_import.status_code, 200)

        data = {
            "investmentDate": "2019-11-28",
            "cdbRate": 103.5,
            "currentDate": "2019-12-03"
        }
        request = self.factory.post('api/v1/calc/', data, content_type='application/json')
        response = calc(request)
        self.assertEqual(response.status_code, 200)
