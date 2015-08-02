# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_auto_20150802_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]
