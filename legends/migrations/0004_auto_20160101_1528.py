# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ('legends', '0003_auto_20151231_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='legend',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='legend',
            name='gender',
            field=models.CharField(default='N', max_length=1,
                                   choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neutral')]),
        ),
        migrations.AddField(
            model_name='legend',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='legend',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, verbose_name='occupation(s)'),
        ),
        migrations.AddField(
            model_name='legend',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
