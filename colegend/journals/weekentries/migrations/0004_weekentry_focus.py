# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekentries', '0003_auto_20161022_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekentry',
            name='focus',
            field=models.TextField(blank=True),
        ),
    ]