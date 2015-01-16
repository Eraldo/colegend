# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import lib.models
import lib.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackers', '0005_sleep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField(validators=[lib.validators.validate_datetime_in_past])),
                ('end', models.DateTimeField(validators=[lib.validators.validate_datetime_in_past], null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
    ]
