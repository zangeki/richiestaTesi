# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-11 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20170809_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerta',
            name='durata',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=False,
        ),
    ]
