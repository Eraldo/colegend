# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0010_auto_20150121_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='joke',
            options={'ordering': ['-rating']},
        ),
    ]
