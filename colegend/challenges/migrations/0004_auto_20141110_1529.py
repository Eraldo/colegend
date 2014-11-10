# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_category_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='category_new',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='category',
            field=models.ForeignKey(to='categories.Category'),
        ),
    ]
