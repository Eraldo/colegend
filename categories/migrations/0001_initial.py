# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
