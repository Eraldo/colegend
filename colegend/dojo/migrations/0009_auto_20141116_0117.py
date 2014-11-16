# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0008_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='_content_rendered',
            field=models.TextField(editable=False, blank=True, default='-'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='module',
            name='content',
            field=markitup.fields.MarkupField(no_rendered_field=True, help_text='A compact explanation of the theory or concept followed by an exercise.'),
            preserve_default=True,
        ),
    ]
