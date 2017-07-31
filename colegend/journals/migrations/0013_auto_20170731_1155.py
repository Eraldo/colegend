# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 09:55
from __future__ import unicode_literals

from django.db import migrations
from django.utils import timezone


def get_extra_content(entry):
    content = ''
    if hasattr(entry, 'focus'):
        content += 'Focus: {focus}\n\n'.format(focus=entry.focus)
    if hasattr(entry, 'locations'):
        content += 'Locations: {locations}\n\n'.format(locations=entry.locations)
    if entry.content:
        content += entry.content
    return content


def migrate_old_to_new_journal_entries(apps, schema_editor):
    JournalEntry = apps.get_model('journals', 'JournalEntry')
    #
    # DayEntry = apps.get_model('dayentries', 'DayEntry')
    # for entry in DayEntry.objects.all():
    #     new_entry = JournalEntry.objects.create(
    #         scope='day',
    #         owner=entry.journal.owner,
    #         start=entry.date,
    #         content=get_extra_content(entry),
    #         keywords=entry.keywords,
    #         created=entry.created
    #     )
    #     new_entry.tags = entry.tags.all()
    #     new_entry.save()
    #
    # WeekEntry = apps.get_model('weekentries', 'WeekEntry')
    # for entry in WeekEntry.objects.all():
    #     start = timezone.datetime.strptime('{}-W{}-1'.format(entry.year, entry.week), "%Y-W%W-%w").date()
    #     new_entry = JournalEntry.objects.create(
    #         scope='week',
    #         owner=entry.journal.owner,
    #         start=start,
    #         content=get_extra_content(entry),
    #         keywords=entry.keywords,
    #         created=entry.created
    #     )
    #     new_entry.tags = entry.tags.all()
    #     new_entry.save()
    #
    # MonthEntry = apps.get_model('monthentries', 'MonthEntry')
    # for entry in MonthEntry.objects.all():
    #     start = timezone.datetime.strptime('{}-M{}'.format(entry.year, entry.month), "%Y-M%m").date()
    #     new_entry = JournalEntry.objects.create(
    #         scope='month',
    #         owner=entry.journal.owner,
    #         start=start,
    #         content=get_extra_content(entry),
    #         keywords=entry.keywords,
    #         created=entry.created
    #     )
    #     new_entry.tags = entry.tags.all()
    #     new_entry.save()


class Migration(migrations.Migration):
    dependencies = [
        ('journals', '0012_journalentry_keywords'),
    ]

    operations = [
        migrations.RunPython(migrate_old_to_new_journal_entries),
    ]
