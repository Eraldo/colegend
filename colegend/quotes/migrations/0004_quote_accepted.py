# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_quote_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='accepted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
