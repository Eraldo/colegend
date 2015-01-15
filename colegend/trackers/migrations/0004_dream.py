# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.models
import django.utils.timezone
import markitup.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackers', '0003_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100)),
                ('description', markitup.fields.MarkupField(blank=True, no_rendered_field=True)),
                ('symbols', models.CharField(blank=True, max_length=100, help_text='Topics? Nouns?')),
                ('_description_rendered', models.TextField(blank=True, editable=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
    ]
