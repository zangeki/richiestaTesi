# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_auto_20171020_0734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studente',
            old_name='assegnatoAproposta',
            new_name='isAssegnato',
        ),
    ]
