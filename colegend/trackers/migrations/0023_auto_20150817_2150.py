# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0022_auto_20150723_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='weight',
            field=models.DecimalField(help_text='Weight in kilograms.', decimal_places=2, max_digits=5),
        ),
    ]
