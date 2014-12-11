# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_user_is_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='keyboard',
            field=models.BooleanField(default=False, verbose_name='Keyboard Control'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='sound',
            field=models.BooleanField(default=True, verbose_name='Sound'),
            preserve_default=True,
        ),
    ]
