# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0005_dayentry_focus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
