# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0008_auto_20140923_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='used_as_daily',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
