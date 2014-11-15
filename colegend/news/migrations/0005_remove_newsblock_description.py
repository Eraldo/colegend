# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_fill_content_with_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsblock',
            name='description',
        ),
    ]
