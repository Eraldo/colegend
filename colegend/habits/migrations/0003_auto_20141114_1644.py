# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_auto_20141023_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='tags',
            field=models.ManyToManyField(null=True, blank=True, related_name='habits', to='tags.Tag', help_text="<a href='/tags/new/' target='_blank'><i class='fa fa-plus-circle' style='color: green;'></i> New Tag</a>- <small>*Refresh page to view new tag.</small><br>"),
        ),
    ]
