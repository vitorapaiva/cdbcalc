# Create your views here.
import codecs
import csv
import datetime
from urllib.request import urlopen

from importcdi.models import CDIHistory


class TreatFileData:
    def treat_file_data(self, array_data):
        cdi_date = datetime.datetime.strptime(array_data[1], '%d/%m/%Y').strftime('%Y-%m-%d')
        result = CDIHistory(cdi_date=cdi_date, cdi_tax_rate=float(array_data[2]))
        return result

    def get_file_data_from_url(self, file_url):
        url_response = urlopen(file_url)
        file_data = csv.reader(codecs.iterdecode(url_response, 'utf-8'))
        file_rows = list(file_data)
        file_header = file_rows.pop(0)
        cdi_data = *map(self.treat_file_data, file_rows),
        return cdi_data
