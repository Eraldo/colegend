# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0020_auto_20150210_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdata',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[lib.validators.validate_date_today_or_in_past, lib.validators.validate_date_within_one_month]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='numberdata',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[lib.validators.validate_date_today_or_in_past, lib.validators.validate_date_within_one_month]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ratingdata',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, validators=[lib.validators.validate_date_today_or_in_past, lib.validators.validate_date_within_one_month]),
            preserve_default=True,
        ),
    ]
