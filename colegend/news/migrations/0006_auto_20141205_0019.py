# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_newsblock_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsblock',
            options={'ordering': ['-sticky', '-date']},
        ),
        migrations.AddField(
            model_name='newsblock',
            name='sticky',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
