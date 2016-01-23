# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('continuous', '0003_continuous_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuous',
            name='dear_diary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='continuous',
            name='entering_leyenda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='continuous',
            name='the_journal',
            field=models.BooleanField(default=False),
        ),
    ]
