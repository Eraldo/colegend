# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('continuous', '0002_continuous_prologue_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuous',
            name='chapter',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
