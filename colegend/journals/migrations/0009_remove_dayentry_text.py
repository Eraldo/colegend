# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0008_fill_content_with_text_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dayentry',
            name='text',
        ),
    ]
