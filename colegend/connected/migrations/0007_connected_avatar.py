# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('connected', '0006_auto_20160112_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='connected',
            name='avatar',
            field=models.BooleanField(default=False),
        ),
    ]
