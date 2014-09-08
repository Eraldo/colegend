# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import lib.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('text', models.TextField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'Day Entries',
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='dayentry',
            unique_together=set([('owner', 'date')]),
        ),
    ]
