# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20151031_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Legends', 'verbose_name': 'Legend'},
        ),
    ]
