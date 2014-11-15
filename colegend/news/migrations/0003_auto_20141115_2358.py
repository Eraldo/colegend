# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20141110_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblock',
            name='_content_rendered',
            field=models.TextField(editable=False, default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsblock',
            name='content',
            field=markitup.fields.MarkupField(no_rendered_field=True, default='', blank=True),
            preserve_default=False,
        ),
    ]
