# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170808_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='azienda',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='azienda',
            name='sede',
            field=models.CharField(max_length=200),
        ),
    ]
