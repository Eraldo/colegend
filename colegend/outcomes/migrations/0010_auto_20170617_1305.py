# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 11:05
from __future__ import unicode_literals

from django.db import migrations, models


def update_outcome_data(apps, schema_editor):
    Outcome = apps.get_model('outcomes', 'Outcome')
    for outcome in Outcome.objects.all():
        outcome.status += 1
        outcome.save()


class Migration(migrations.Migration):

    dependencies = [
        ('outcomes', '0009_auto_20170609_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'open'), (2, 'waiting'), (3, 'done'), (4, 'canceled')], default=1, verbose_name='status'),
        ),
        migrations.RunPython(update_outcome_data),
    ]