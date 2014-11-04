# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_user_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, help_text="Designates whether the user can access the site's management features.", verbose_name='manager'),
            preserve_default=True,
        ),
    ]
