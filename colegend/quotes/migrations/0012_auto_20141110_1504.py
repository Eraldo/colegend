# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0011_quote_category_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='category_new',
        ),
        migrations.AlterField(
            model_name='quote',
            name='category',
            field=models.ForeignKey(to='categories.Category'),
        ),
    ]
