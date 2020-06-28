from django.test import RequestFactory, TestCase

from importcdi.views import import_cdi


class TestImport(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_import(self):
        data = {'url': "https://gorila-blog.s3-us-west-2.amazonaws.com/CDI_Prices.csv"}
        request = self.factory.post('cdi/import', data, content_type='application/json')
        response = import_cdi(request)
        self.assertEqual(response.status_code, 200)

    def test_import_duplicate(self):
        data = {'url': "https://gorila-blog.s3-us-west-2.amazonaws.com/CDI_Prices.csv"}
        request = self.factory.post('cdi/import', data, content_type='application/json')
        response1 = import_cdi(request)
        response2 = import_cdi(request)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 400)
