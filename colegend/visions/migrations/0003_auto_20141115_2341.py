# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visions', '0002_auto_20140908_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vision',
            name='description',
        ),
        migrations.AddField(
            model_name='vision',
            name='_content_rendered',
            field=models.TextField(editable=False, blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vision',
            name='content',
            field=markitup.fields.MarkupField(blank=True, default='', no_rendered_field=True),
            preserve_default=False,
        ),
    ]
