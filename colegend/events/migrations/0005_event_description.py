# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='short description'),
        ),
    ]