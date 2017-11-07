# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-08 22:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0002_focus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='focus',
            options={'ordering': ['start'], 'verbose_name': 'Focus outcomes', 'verbose_name_plural': 'Focus Outcomes'},
        ),
        migrations.AlterField(
            model_name='focus',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_focuses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='focus',
            unique_together=set([('owner', 'scope', 'start')]),
        ),
    ]