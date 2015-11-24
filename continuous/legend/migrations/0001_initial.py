# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import annoying.fields
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20151031_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legend',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner',
                 annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('prologue', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]