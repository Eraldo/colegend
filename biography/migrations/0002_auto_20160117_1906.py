# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('biography', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biography',
            old_name='biography',
            new_name='text',
        ),
    ]
