# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OuterCall',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('trigger', models.TextField(verbose_name='How did you find out about coLegend?')),
                ('referrer', models.CharField(max_length=255, blank=True, verbose_name='Who was your contact person?',
                                              help_text='If someone told you about coLegend: Who was it?')),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
