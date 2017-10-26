# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20171004_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposta',
            name='archiviata',
        ),
        migrations.RemoveField(
            model_name='proposta',
            name='inRichiesta',
        ),
        migrations.RemoveField(
            model_name='proposta',
            name='richiedibile',
        ),
        migrations.AddField(
            model_name='proposta',
            name='macrostato',
            field=models.CharField(choices=[('proposta richiedibile', ' proposta richiedibile'), (' proposta non richiedibile', ' proposta non richiedibile')], default=('proposta richiedibile', ' proposta richiedibile'), max_length=100),
        ),
        migrations.AddField(
            model_name='proposta',
            name='stato',
            field=models.CharField(choices=[('proposta senza richieste', 'proposta senza richieste'), ('proposta con richieste', 'proposta con richieste'), ('proposta assegnata', 'proposta assegnata'), ('proposta archiviata', 'proposta archiviata')], default=('proposta senza richieste', 'proposta senza richieste'), max_length=100),
        ),
    ]
