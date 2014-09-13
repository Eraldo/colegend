# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('type', models.CharField(choices=[('open', 'open'), ('closed', 'closed')], default='open', max_length=50)),
                ('order', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Statuses',
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
