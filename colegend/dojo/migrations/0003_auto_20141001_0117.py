# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0002_auto_20141001_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(help_text='A compact description of the theory or concept followed by an exercise.'),
        ),
    ]
