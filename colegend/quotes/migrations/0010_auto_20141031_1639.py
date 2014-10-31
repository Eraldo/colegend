# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0009_quote_used_as_daily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='used_as_daily',
            field=models.DateField(unique=True, blank=True, null=True),
        ),
    ]
