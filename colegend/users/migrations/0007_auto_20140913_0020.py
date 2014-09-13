# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20140912_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_tester',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='foo@bar.com', max_length=75, verbose_name='email address', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='foo', max_length=30, verbose_name='first name', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='bar', max_length=30, verbose_name='last name', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'),
        ),
    ]
