# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0003_auto_20141001_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='source',
            field=models.TextField(blank=True, help_text='Where is the content from? URL? Author?', default=''),
            preserve_default=False,
        ),
    ]
