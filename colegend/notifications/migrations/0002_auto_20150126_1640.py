# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='_description_rendered',
            field=models.TextField(blank=True, default='', editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=markitup.fields.MarkupField(blank=True, no_rendered_field=True),
            preserve_default=True,
        ),
    ]
