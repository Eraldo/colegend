# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 17:14
from __future__ import unicode_literals

import colegend.cms.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160711_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventspage',
            name='content',
            field=wagtail.core.fields.StreamField((('heading', colegend.cms.blocks.HeadingBlock()), ('rich_text', colegend.cms.blocks.RichTextBlock()), ('image', colegend.cms.blocks.ImageBlock()), ('embed', colegend.cms.blocks.EmbedBlock()), ('html', wagtail.core.blocks.RawHTMLBlock())), blank=True),
        ),
    ]
