# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20141116_1058'),
        ('journals', '0017_auto_20150117_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayentry',
            name='tags',
            field=models.ManyToManyField(related_name='journals', blank=True, to='tags.Tag', null=True),
            preserve_default=True,
        ),
    ]
