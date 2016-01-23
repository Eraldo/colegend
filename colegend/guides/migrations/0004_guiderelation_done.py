# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('guides', '0003_remove_guiderelation_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='guiderelation',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Guiding is done'),
        ),
    ]
