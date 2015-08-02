# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0018_dayentry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='journals', to='tags.Tag'),
        ),
    ]
