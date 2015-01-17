# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('trackers', '0006_walk'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=7, to='categories.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='end_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='feedback',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='origin',
            field=models.CharField(max_length=100, default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='start_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
