# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('connected', '0004_auto_20151221_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connected',
            old_name='legend',
            new_name='me',
        ),
        migrations.RemoveField(
            model_name='connected',
            name='legend_introduction',
        ),
    ]
