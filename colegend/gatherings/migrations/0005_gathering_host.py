# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gatherings', '0004_auto_20141110_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='host',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=4),
            preserve_default=False,
        ),
    ]
