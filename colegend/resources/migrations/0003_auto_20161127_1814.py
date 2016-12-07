# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 17:14
from __future__ import unicode_literals

import colegend.cms.blocks
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20161017_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', colegend.cms.blocks.HeadingBlock()), ('rich_text', colegend.cms.blocks.RichTextBlock()), ('image', colegend.cms.blocks.ImageBlock()), ('embed', colegend.cms.blocks.EmbedBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock())), blank=True),
        ),
        migrations.AlterField(
            model_name='resourcespage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', colegend.cms.blocks.HeadingBlock()), ('rich_text', colegend.cms.blocks.RichTextBlock()), ('image', colegend.cms.blocks.ImageBlock()), ('embed', colegend.cms.blocks.EmbedBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock())), blank=True),
        ),
    ]