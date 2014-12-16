# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def update_journal_owner(apps, schema_editor):
        entry_class = apps.get_model("journals", "DayEntry")
        for entry in entry_class.objects.all():
            user = entry.owner
            journal = user.journal
            journal.owner = user
            journal.save()

    def update_journal_entries(apps, schema_editor):
        journal_class = apps.get_model("journals", "Journal")
        for journal in journal_class.objects.all():
            journal.entries = journal.owner.dayentry_set.all()
            journal.save()

    dependencies = [
        ('journals', '0010_auto_20141216_2122'),
    ]

    operations = [
        migrations.RunPython(update_journal_owner),
        migrations.RunPython(update_journal_entries),
    ]
