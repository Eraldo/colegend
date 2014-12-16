# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0011_auto_20141216_2123'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dayentry',
            unique_together=set([('journal', 'date')]),
        ),
    ]
