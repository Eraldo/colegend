# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 21:21
from __future__ import unicode_literals

import colegend.cms.blocks
from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_aboutpage_complete_teaser_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='content',
            field=wagtail.core.fields.StreamField((('heading', colegend.cms.blocks.HeadingBlock()), ('rich_text', colegend.cms.blocks.RichTextBlock()), ('image', colegend.cms.blocks.ImageBlock()), ('embed', colegend.cms.blocks.EmbedBlock())), blank=True),
        ),
    ]
