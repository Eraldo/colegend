# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20140914_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('owner', annoying.fields.AutoOneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('language', models.CharField(default='EN', choices=[('EN', 'English')], max_length=2)),
                ('day_start', models.PositiveSmallIntegerField(default=0, verbose_name='Custom day start time', max_length=24, help_text='When does your day start? Enter number between 0 and 24 (24h clock).')),
                ('sound', models.BooleanField(default=True, verbose_name='Sound enabled')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
