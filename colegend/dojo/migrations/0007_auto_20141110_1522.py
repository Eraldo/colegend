# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0006_module_category_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='category_new',
        ),
        migrations.AlterField(
            model_name='module',
            name='category',
            field=models.ForeignKey(to='categories.Category'),
        ),
    ]
