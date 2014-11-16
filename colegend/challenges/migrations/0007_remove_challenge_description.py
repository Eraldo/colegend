# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_fill_content_with_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='description',
        ),
    ]
