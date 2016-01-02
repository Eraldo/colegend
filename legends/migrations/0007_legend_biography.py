# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('legends', '0006_auto_20160101_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='biography',
            field=models.TextField(blank=True),
        ),
    ]
