# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0006_auto_20141021_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayentry',
            name='_content_rendered',
            field=models.TextField(default='-', blank=True, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayentry',
            name='content',
            field=markitup.fields.MarkupField(default='-', no_rendered_field=True),
            preserve_default=False,
        ),
    ]
