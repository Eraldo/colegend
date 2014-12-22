# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_feature_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='features', default=''),
            preserve_default=False,
        ),
    ]
