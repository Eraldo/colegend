# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('tasks', '0012_auto_20141226_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, to='categories.Category', null=True),
            preserve_default=True,
        ),
    ]
