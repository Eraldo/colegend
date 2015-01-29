# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import lib.models
import lib.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackers', '0014_auto_20150122_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, validators=[lib.validators.validate_date_today_or_in_past, lib.validators.validate_date_within_one_week])),
            ],
            options={
                'abstract': False,
                'ordering': ['-date'],
            },
            bases=(lib.models.ValidateModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NumberData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, validators=[lib.validators.validate_date_today_or_in_past, lib.validators.validate_date_within_one_week])),
                ('number', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'ordering': ['-date'],
            },
            bases=(lib.models.ValidateModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RatingData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, validators=[lib.validators.validate_date_today_or_in_past, lib.validators.validate_date_within_one_week])),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'abstract': False,
                'ordering': ['-date'],
            },
            bases=(lib.models.ValidateModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('tracker_type', models.PositiveSmallIntegerField(choices=[(0, 'Check'), (1, 'Number'), (2, 'Rating')], verbose_name='Type', default=0)),
                ('frequency', models.PositiveSmallIntegerField(choices=[(1, 'Daily'), (2, 'Weekly'), (3, 'Monthly'), (0, 'Unknown')], default=1)),
                ('category', models.ForeignKey(to='categories.Category')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(lib.models.AutoUrlMixin, models.Model),
        ),
        migrations.AddField(
            model_name='ratingdata',
            name='tracker',
            field=models.ForeignKey(to='trackers.Tracker'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='ratingdata',
            unique_together=set([('tracker', 'date')]),
        ),
        migrations.AddField(
            model_name='numberdata',
            name='tracker',
            field=models.ForeignKey(to='trackers.Tracker'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='numberdata',
            unique_together=set([('tracker', 'date')]),
        ),
        migrations.AddField(
            model_name='checkdata',
            name='tracker',
            field=models.ForeignKey(to='trackers.Tracker'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='checkdata',
            unique_together=set([('tracker', 'date')]),
        ),
    ]
