# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideRelation',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner',
                 annoying.fields.AutoOneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('outer_call_checked', models.BooleanField(default=False, verbose_name='Talked about Outer Call')),
                ('inner_call_checked', models.BooleanField(default=False, verbose_name='Talked about Inner Call')),
                ('coLegend_checked',
                 models.BooleanField(default=False, verbose_name='Answered any questions about coLegend')),
                ('guiding_checked', models.BooleanField(default=False, verbose_name='Talked about becoming a Guide')),
                ('guide', models.ForeignKey(null=True, related_name='guidee_relations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
