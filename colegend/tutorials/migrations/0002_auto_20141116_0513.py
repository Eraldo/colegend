# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='_description_rendered',
            field=models.TextField(editable=False, blank=True, default='-'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=markitup.fields.MarkupField(no_rendered_field=True, help_text='What is the idea? How to use the current implementation.'),
            preserve_default=True,
        ),
    ]
