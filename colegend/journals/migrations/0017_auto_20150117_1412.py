# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def migrate_data(apps, schema_editor):
    """
    Migrate journal template from general settings to journal model.
    """
    journal_cls = apps.get_model("journals", "Journal")
    for journal in journal_cls.objects.all():
        owner = journal.owner
        old_template = owner.settings.journal_entry_template
        journal.template = old_template
        journal.save()


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0016_journal_template'),
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
