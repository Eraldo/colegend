# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('innercall', '0002_auto_20151225_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innercall',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
