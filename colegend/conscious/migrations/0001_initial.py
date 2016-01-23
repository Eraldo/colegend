# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import annoying.fields
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conscious',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner',
                 annoying.fields.AutoOneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'conscious path',
                'verbose_name_plural': 'conscious path',
            },
        ),
    ]
