# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0007_auto_20140923_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='name',
            field=models.CharField(max_length=100, unique=True, help_text='What is the quote about?'),
        ),
    ]
