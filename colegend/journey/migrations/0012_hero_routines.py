# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-09 11:52
from __future__ import unicode_literals

import colegend.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0011_auto_20180130_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='routines',
            field=colegend.core.fields.MarkdownField(blank=True),
        ),
    ]
