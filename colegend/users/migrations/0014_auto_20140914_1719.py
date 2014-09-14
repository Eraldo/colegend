# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20140914_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='firstname', blank=True, verbose_name='first name', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='lastname', blank=True, verbose_name='last name', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
