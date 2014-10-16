# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0004_auto_20141016_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayentry',
            name='focus',
            field=models.CharField(default='', max_length=100, help_text='What was the most important experience/topic on this day?'),
            preserve_default=False,
        ),
    ]
