# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20171004_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='tipologia',
            field=models.CharField(choices=[('Tesi', 'Tesi'), ('Attività progettuale', 'Attività progettuale')], max_length=50),
        ),
    ]
