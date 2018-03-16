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
            name='InnerCall',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('motivation', models.TextField(verbose_name='What was your motivation to join coLegend?')),
                ('change', models.TextField(verbose_name='What do you want to change in your life?')),
                ('drive', models.PositiveIntegerField(verbose_name='How strong is your drive to get there?',
                                                      help_text='10 = very strong, 1 = not strong at all')),
                ('wishes', models.TextField(verbose_name='What are your wishes for this platform?')),
                ('other', models.TextField(verbose_name='Is there anything else you want to share? :)')),
                ('owner', models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
