# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20140924_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(null=True, blank=True, related_name='projects', to='tags.Tag', help_text="<a href='/tags/new/' target='_blank'><i class='fa fa-plus-circle' style='color: green;'></i> New Tag</a>- <small>*Refresh page to view new tag.</small><br>"),
        ),
    ]
