# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='role',
            field=models.CharField(max_length=2, default='OP', verbose_name='System Role', choices=[('ME', 'Mentor'), ('MA', 'Manager'), ('MO', 'Motivator'), ('OP', 'Operator')]),
            preserve_default=True,
        ),
    ]
