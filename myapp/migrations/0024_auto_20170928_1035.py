# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-28 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_proposta_azienda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offerta',
            old_name='pubblicata',
            new_name='archiviata',
        ),
    ]
