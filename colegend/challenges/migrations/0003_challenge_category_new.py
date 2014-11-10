# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('challenges', '0002_auto_20141030_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='category_new',
            field=models.ForeignKey(to='categories.Category', default=1),
            preserve_default=False,
        ),
    ]
