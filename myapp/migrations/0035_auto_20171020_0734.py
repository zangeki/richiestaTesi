# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20171018_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='studente',
            name='assegnatoAproposta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='offerta',
            name='macrostato',
            field=models.CharField(choices=[('offerta richiedibile', ' offerta richiedibile'), ('offerta non richiedibile', ' offerta non richiedibile')], default='offerta non richiedibile', max_length=100),
        ),
    ]