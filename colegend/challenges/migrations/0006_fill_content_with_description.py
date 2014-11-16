# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def combine_names(apps, schema_editor):
        challenge_class = apps.get_model("challenges", "Challenge")
        for challenge in challenge_class.objects.all():
            challenge.content = challenge.description
            challenge.save()

    dependencies = [
        ('challenges', '0005_auto_20141116_0019'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
