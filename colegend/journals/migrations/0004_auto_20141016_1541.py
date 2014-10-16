# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import journals.models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0003_dayentry_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='location',
            field=models.CharField(max_length=100, default=journals.models.get_last_location),
        ),
    ]
