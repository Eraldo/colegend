# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0021_auto_20150414_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkdata',
            name='notes',
            field=models.CharField(max_length=100, blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='numberdata',
            name='notes',
            field=models.CharField(max_length=100, blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratingdata',
            name='notes',
            field=models.CharField(max_length=100, blank=True, default=''),
            preserve_default=False,
        ),
    ]
