# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_docente_codice'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerta',
            name='titolo',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proposta',
            name='titolo',
            field=models.CharField(max_length=200),
        ),
    ]