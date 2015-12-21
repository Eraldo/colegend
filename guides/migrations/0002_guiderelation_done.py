# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guiderelation',
            name='done',
            field=models.BooleanField(verbose_name='Guiding process is done', default=False),
        ),
    ]
