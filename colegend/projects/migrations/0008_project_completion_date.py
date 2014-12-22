# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20141221_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
