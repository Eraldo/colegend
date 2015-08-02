# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_auto_20141221_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='habits', to='tags.Tag'),
        ),
    ]
