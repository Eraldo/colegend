# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '__first__'),
        ('projects', '0001_initial'),
        ('statuses', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(blank=True, help_text='When will I start?', null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='projects.Project', null=True, blank=True, related_name='tasks')),
                ('status', models.ForeignKey(to='statuses.Status', default=1)),
                ('tags', models.ManyToManyField(to='tags.Tag', blank=True, related_name='tasks', null=True)),
            ],
            options={
                'ordering': ['project', 'name'],
            },
            bases=(lib.models.ValidateModelMixin, lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set([('owner', 'project', 'name')]),
        ),
    ]
