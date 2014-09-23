# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_auto_20140922_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=100, default='Someone'),
        ),
    ]
