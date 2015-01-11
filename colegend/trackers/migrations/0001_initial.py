# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import lib.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Next'), (1, 'Todo'), (2, 'Maybe'), (3, 'Done'), (4, 'Canceled')], default=1)),
                ('notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['status'],
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.PositiveSmallIntegerField(default=1)),
                ('person', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'Sex',
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.PositiveSmallIntegerField()),
                ('notes', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
                'verbose_name_plural': 'Weight',
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
    ]
