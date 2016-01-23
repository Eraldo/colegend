# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='role',
            name='nickname',
            field=models.CharField(verbose_name='nickname', max_length=255, blank=True),
        ),
    ]
