# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['status', '-modification_date']},
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(help_text='When will I start/continue?', null=True, blank=True),
            preserve_default=True,
        ),
    ]
