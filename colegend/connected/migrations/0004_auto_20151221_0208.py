# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('connected', '0003_auto_20151221_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='connected',
            name='legend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='connected',
            name='legend_introduction',
            field=models.BooleanField(default=False),
        ),
    ]
