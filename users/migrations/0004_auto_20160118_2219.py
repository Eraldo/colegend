# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_user_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='checkpoints',
            field=models.ManyToManyField(to='checkpoints.Checkpoint', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='roles.Role', blank=True),
        ),
    ]
