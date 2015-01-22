# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0013_auto_20150122_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['status', '-rating']},
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], default=0),
            preserve_default=True,
        ),
    ]
