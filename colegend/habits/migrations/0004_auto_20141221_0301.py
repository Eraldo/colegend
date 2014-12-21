# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_auto_20141114_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag', blank=True, null=True, related_name='habits'),
            preserve_default=True,
        ),
    ]
