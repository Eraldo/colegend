# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0007_auto_20141110_1522'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
