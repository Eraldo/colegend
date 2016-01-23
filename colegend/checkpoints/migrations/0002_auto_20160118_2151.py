# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('checkpoints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpoint',
            name='name',
            field=models.CharField(verbose_name='name', unique=True, max_length=255),
        ),
    ]
