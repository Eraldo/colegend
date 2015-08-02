# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_settings_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='email address', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_name='user_set', related_query_name='user', to='auth.Group', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
        ),
    ]
