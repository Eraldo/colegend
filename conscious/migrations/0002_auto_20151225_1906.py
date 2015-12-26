# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('conscious', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conscious',
            name='inner_call',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='conscious',
            name='outer_call',
            field=models.BooleanField(default=False),
        ),
    ]
