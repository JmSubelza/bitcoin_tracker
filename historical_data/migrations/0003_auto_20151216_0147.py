# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 01:47
from __future__ import unicode_literals

from django.db import migrations
from datetime import date


def load_data(apps, schema_editor):

    PriceHistory = apps.get_model("historical_data", "PriceHistory")

    PriceHistory(date=date(2013,11,29),
                 price=1234.00,
                 volume=354564,
                 total_btc=12054375,
                 market_cap=1,
                 ).save()
    PriceHistory(date=date(2012,11,29),
                 price=12.15,
                 volume=187947,
                 total_btc=10504650,
                 market_cap=2,
                 ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('historical_data', '0002_secofnmigrations'),
    ]

    operations = [

        migrations.RunPython(load_data)
    ]
