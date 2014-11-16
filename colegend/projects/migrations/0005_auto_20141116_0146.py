# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20141114_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='_description_rendered',
            field=models.TextField(default='', blank=True, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=markitup.fields.MarkupField(blank=True, no_rendered_field=True),
            preserve_default=True,
        ),
    ]
