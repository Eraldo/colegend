# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20140912_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        ),
    ]
