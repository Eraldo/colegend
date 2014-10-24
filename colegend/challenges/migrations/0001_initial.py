# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0005_auto_20141001_1535'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='A short description of the course content.')),
                ('source', models.TextField(help_text='Where is the content from? URL? Author?', blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='dojo.Category')),
                ('provider', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
