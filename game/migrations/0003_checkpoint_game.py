# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
import annoying.fields
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_remove_user_name'),
        ('game', '0002_auto_20160109_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('owner',
                 annoying.fields.AutoOneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('checkpoints', models.ManyToManyField(to='game.Checkpoint', blank=True)),
                ('completed', models.ManyToManyField(to='game.Card', related_name='games_completed', blank=True)),
                ('hand', models.ManyToManyField(to='game.Card', related_name='games_hand', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
