# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_settings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterField(
            model_name='settings',
            name='day_start',
            field=models.PositiveSmallIntegerField(verbose_name='Day start time', default=0, validators=[django.core.validators.MaxValueValidator(24)], help_text='When does your day start? Enter number between 0 and 24 (24h clock).'),
        ),
    ]
