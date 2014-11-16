# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_auto_20141110_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='_content_rendered',
            field=models.TextField(editable=False, default='-', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='content',
            field=markitup.fields.MarkupField(default='-', help_text='What is this challenge about? How can I do this challenge?', no_rendered_field=True),
            preserve_default=False,
        ),
    ]
