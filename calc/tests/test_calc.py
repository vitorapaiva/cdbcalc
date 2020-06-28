from django.test import RequestFactory, TestCase

from calc.views import calc


class TestCalc(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_calc(self):
        data = {
            "investmentDate": "2019-11-28",
            "cdbRate": 103.5,
            "currentDate": "2019-12-03"
        }
        request = self.factory.post('calc/', data, content_type='application/json')
        response = calc(request)
        self.assertEqual(response.status_code, 200)
        print(response.content)
