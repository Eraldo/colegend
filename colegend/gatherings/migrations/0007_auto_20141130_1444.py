# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


def migrate_data(apps, schema_editor):
    gathering_cls = apps.get_model("gatherings", "Gathering")
    for gathering in gathering_cls.objects.all():
        gathering.start = gathering.date
        gathering.end = gathering.date + timezone.timedelta(hours=1)
        gathering.save()


class Migration(migrations.Migration):
    dependencies = [
        ('gatherings', '0006_auto_20141130_1439'),
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
