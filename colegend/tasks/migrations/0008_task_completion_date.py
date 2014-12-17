# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20141116_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
