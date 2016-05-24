# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-24 20:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('outcomes', '0004_auto_20160524_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 24, 20, 1, 20, 468558, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outcome',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 5, 24, 20, 1, 30, 100063, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
