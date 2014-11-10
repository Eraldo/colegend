# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('quotes', '0010_auto_20141031_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='category_new',
            field=models.ForeignKey(default=1, to='categories.Category'),
            preserve_default=False,
        ),
    ]
