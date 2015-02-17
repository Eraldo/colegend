# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('tags', '0002_auto_20141116_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(null=True, to='categories.Category', blank=True),
            preserve_default=True,
        ),
    ]
