# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import easy_thumbnails.fields
import core.utils.media_paths


class Migration(migrations.Migration):
    dependencies = [
        ('legends', '0002_legend_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legend',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True,
                                                               upload_to=core.utils.media_paths.UploadToOwnedDirectory(
                                                                   'legend')),
        ),
    ]
