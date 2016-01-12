# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('connected', '0005_auto_20160101_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connected',
            old_name='me',
            new_name='about',
        ),
        migrations.AddField(
            model_name='connected',
            name='biography',
            field=models.BooleanField(default=False),
        ),
    ]
