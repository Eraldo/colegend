# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True, help_text='Staff notes.', verbose_name='notes'),
        ),
    ]