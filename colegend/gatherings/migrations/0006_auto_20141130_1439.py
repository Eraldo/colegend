# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gatherings', '0005_gathering_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gathering',
            options={'ordering': ['-start']},
        ),
        migrations.AddField(
            model_name='gathering',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 30, 13, 39, 14, 284771, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gathering',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 30, 13, 39, 22, 37014, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
