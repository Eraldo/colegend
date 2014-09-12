# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import lib.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.date(2014, 1, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, default='Linz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=100, default='Austria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=1, default='M', choices=[('M', 'Male Legend ♂'), ('F', 'Female Legend ♀')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_tester',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=lib.modelfields.PhoneField(max_length=16, help_text='Mobile or other phone number. Example: +4369910203039', default='+4369910203039'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.CharField(max_length=5, default='4020'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=100, default='Legendstreet 4'),
            preserve_default=False,
        ),
    ]
