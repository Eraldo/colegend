# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 18:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duo',
            name='members',
        ),
        migrations.AlterField(
            model_name='tribe',
            name='mentor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='tribe', to=settings.AUTH_USER_MODEL, verbose_name='mentor'),
        ),
    ]
