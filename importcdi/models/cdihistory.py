import datetime

from django.db import models


class CDIHistory(models.Model):
    cdi_date = models.DateField('CDI date', unique=True)
    cdi_tax_rate = models.FloatField()

    def __str__(self):
        return self.cdi_date

