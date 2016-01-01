# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('legends', '0004_auto_20160101_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='test',
            field=models.CharField(max_length=1, default=''),
            preserve_default=False,
        ),
    ]
