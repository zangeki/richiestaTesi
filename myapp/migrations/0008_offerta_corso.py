# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-13 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_offerta_durata'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerta',
            name='corso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.Corso'),
            preserve_default=False,
        ),
    ]
