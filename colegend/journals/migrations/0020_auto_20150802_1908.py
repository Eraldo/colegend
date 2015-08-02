# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markitup.fields
import lib.models
import journals.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_tag_category'),
        ('journals', '0019_auto_20150802_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('history', models.TextField(blank=True)),
                ('date', models.DateField(validators=[journals.validators.validate_present_or_past], default=datetime.datetime.today)),
                ('focus', models.CharField(max_length=100, help_text='What was the most important experience/topic on this week?')),
                ('content', markitup.fields.MarkupField(no_rendered_field=True)),
                ('_content_rendered', models.TextField(blank=True, editable=False)),
                ('journal', models.ForeignKey(related_name='week_entries', to='journals.Journal')),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag')),
            ],
            options={
                'verbose_name_plural': 'Week Entries',
                'ordering': ['-date'],
                'default_related_name': 'week_entries',
            },
            bases=(lib.models.ValidateModelMixin, lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='dayentry',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='weekentry',
            unique_together=set([('journal', 'date')]),
        ),
    ]
