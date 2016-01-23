# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):
    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='games/cards/'),
        ),
    ]
