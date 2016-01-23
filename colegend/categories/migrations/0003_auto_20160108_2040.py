# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0002_auto_20160108_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories', 'ordering': ['-order']},
        ),
        migrations.RemoveField(
            model_name='category',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
