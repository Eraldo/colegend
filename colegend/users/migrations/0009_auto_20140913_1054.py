# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20140913_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='email address', max_length=75, blank=True, default='foo@bar.com'),
            preserve_default=False,
        ),
    ]
