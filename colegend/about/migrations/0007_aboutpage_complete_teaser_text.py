# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 16:19
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20160705_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='complete_teaser_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
