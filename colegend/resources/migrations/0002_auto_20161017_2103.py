# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 19:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='area_1',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Health'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='area_2',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Joy'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='area_3',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Power'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='area_4',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Connection'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='area_5',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Expression'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='area_6',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Mind'),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='area_7',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)], verbose_name='Spirit'),
        ),
    ]
