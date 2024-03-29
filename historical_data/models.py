from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.PositiveIntegerField()
    total_btc = models.PositiveIntegerField()
    market_cap = models.PositiveIntegerField(null=True)