# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import journals.validators


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='date',
            field=models.DateField(default=datetime.datetime.today, validators=[journals.validators.validate_present_or_past]),
        ),
    ]
