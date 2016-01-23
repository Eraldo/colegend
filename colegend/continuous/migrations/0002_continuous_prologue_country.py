# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('continuous', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuous',
            name='prologue_country',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
