from django.test import RequestFactory, TestCase

from importcdi.views import importcdi


class TestCalc(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_calc(self):
        request = self.factory.get('/import')
        response = importcdi(request)
        print(response.content)
