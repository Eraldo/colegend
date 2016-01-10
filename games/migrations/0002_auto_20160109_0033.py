# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.ManyToManyField(to='categories.Category', related_name='cards'),
        ),
    ]
