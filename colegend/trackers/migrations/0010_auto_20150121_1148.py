# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0009_auto_20150119_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_date',
            field=models.DateField(null=True, blank=True, validators=[lib.validators.validate_date_today_or_in_past]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='start_date',
            field=models.DateField(null=True, blank=True, validators=[lib.validators.validate_date_today_or_in_past]),
            preserve_default=True,
        ),
    ]
