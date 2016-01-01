# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import easy_thumbnails.fields
import core.utils.media_paths


class Migration(migrations.Migration):
    dependencies = [
        ('legends', '0005_legend_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legend',
            name='test',
        ),
        migrations.AlterField(
            model_name='legend',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='legend',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(
                upload_to=core.utils.media_paths.UploadToOwnedDirectory('legend')),
        ),
        migrations.AlterField(
            model_name='legend',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neutral')]),
        ),
        migrations.AlterField(
            model_name='legend',
            name='name',
            field=models.CharField(help_text='Your full name', verbose_name='name', max_length=255),
        ),
    ]
