# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0012_auto_20141110_1504'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
