# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20140914_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_accepted',
            field=models.DateTimeField(verbose_name='date accepted', blank=True, null=True),
            preserve_default=True,
        ),
    ]
