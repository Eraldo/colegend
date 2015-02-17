# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('projects', '0008_project_completion_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, to='categories.Category', null=True),
            preserve_default=True,
        ),
    ]
