# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 10:55
from __future__ import unicode_literals

import colegend.core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('categories', '0004_load_initial_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               to='categories.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'default_related_name': 'tags',
                'ordering': ['name'],
            },
            bases=(colegend.core.models.AutoUrlsMixin, colegend.core.models.OwnedCheckMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('owner', 'name')]),
        ),
    ]
