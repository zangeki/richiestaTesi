# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 09:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20170918_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerta',
            name='data_pub',
            field=models.DateField(default=datetime.datetime(2017, 9, 19, 9, 59, 15, 374874)),
        ),
    ]
