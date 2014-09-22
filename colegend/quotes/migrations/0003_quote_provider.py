# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0002_auto_20140922_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='provider',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=4),
            preserve_default=False,
        ),
    ]
