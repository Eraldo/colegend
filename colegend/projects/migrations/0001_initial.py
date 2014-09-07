# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '__first__'),
        ('statuses', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(default=1, to='statuses.Status')),
                ('tags', models.ManyToManyField(null=True, related_name='projects', to='tags.Tag', blank=True)),
            ],
            options={
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('owner', 'name')]),
        ),
    ]
