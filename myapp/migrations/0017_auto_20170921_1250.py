# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20170920_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='richiedibile',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='tipologia',
            field=models.CharField(choices=[('Tesi', 'Tesi'), ('Attività progettuale', 'Attività progettuale')], max_length=50),
        ),
    ]
