# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='_description_rendered',
            field=models.TextField(default='', editable=False, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=markitup.fields.MarkupField(no_rendered_field=True, blank=True),
            preserve_default=True,
        ),
    ]
