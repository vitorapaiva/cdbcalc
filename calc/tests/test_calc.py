from django.test import RequestFactory, TestCase

from calc.views import calc


class TestCalc(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_calc(self):
        request = self.factory.get('/calc')
        response = calc(request)
        print(response.content)
