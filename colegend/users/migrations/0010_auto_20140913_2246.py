# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20140913_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_accepted',
            field=models.BooleanField(help_text='Designates whether the user has been accepted by the site managers.', verbose_name='accepted status', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True),
        ),
    ]
