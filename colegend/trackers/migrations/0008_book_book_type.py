# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0007_auto_20150117_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.PositiveSmallIntegerField(verbose_name='Type', default=0, choices=[((0,), 'Book'), ((1,), 'E-Book'), ((2,), 'Audio-Book')]),
            preserve_default=True,
        ),
    ]
