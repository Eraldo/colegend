# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def combine_names(apps, schema_editor):
        entry_class = apps.get_model("journals", "DayEntry")
        for entry in entry_class.objects.all():
            entry.content = entry.text
            entry.save()

    dependencies = [
        ('journals', '0007_auto_20141115_1231'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
