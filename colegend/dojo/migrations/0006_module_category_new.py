# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('dojo', '0005_auto_20141001_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='category_new',
            field=models.ForeignKey(default=1, to='categories.Category'),
            preserve_default=False,
        ),
    ]
