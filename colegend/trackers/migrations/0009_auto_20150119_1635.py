# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0008_book_book_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.PositiveSmallIntegerField(verbose_name='Type', default=0, choices=[(0, 'Book'), (1, 'E-Book'), (2, 'Audio-Book')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='end_date',
            field=models.DateField(blank=True, validators=[lib.validators.validate_datetime_in_past], null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='start_date',
            field=models.DateField(blank=True, validators=[lib.validators.validate_datetime_in_past], null=True),
            preserve_default=True,
        ),
    ]
