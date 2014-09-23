# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_auto_20140923_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(),
        ),
    ]
