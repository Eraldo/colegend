# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.validators
import lib.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackers', '0004_dream'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField(validators=[lib.validators.validate_datetime_in_past])),
                ('end', models.DateTimeField(blank=True, validators=[lib.validators.validate_datetime_in_past], null=True)),
                ('notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
    ]
