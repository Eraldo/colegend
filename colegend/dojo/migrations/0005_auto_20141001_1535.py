# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0004_module_source'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-pk'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='module',
            name='content',
            field=models.TextField(default='', help_text='A compact explanation of the theory or concept followed by an exercise.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(help_text='A short description of the course content.'),
        ),
    ]
