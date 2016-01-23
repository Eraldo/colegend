# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('guides', '0002_guiderelation_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guiderelation',
            name='done',
        ),
    ]
