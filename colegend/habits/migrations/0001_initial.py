# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import lib.models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('routines', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('routine', models.ForeignKey(null=True, blank=True, related_name='habits', to='routines.Routine')),
                ('tags', models.ManyToManyField(null=True, related_name='habits', blank=True, to='tags.Tag')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='habit',
            unique_together=set([('owner', 'name')]),
        ),
    ]
