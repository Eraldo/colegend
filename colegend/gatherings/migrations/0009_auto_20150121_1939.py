# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import markitup.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gatherings', '0008_remove_gathering_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='_notes_rendered',
            field=models.TextField(blank=True, default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gathering',
            name='notes',
            field=markitup.fields.MarkupField(blank=True, default='', no_rendered_field=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gathering',
            name='participants',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='gatherings_participated'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gathering',
            name='topic',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]
