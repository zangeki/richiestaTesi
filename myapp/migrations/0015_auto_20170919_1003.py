# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_offerta_data_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerta',
            name='data_pub',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
