# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('legends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='avatar',
            field=models.ImageField(upload_to='', blank=True),
        ),
    ]
