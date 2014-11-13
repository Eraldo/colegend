# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(help_text='What is the idea? How to use the current implementation.')),
            ],
            options={
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
    ]
