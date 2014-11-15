# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def combine_names(apps, schema_editor):
        block_class = apps.get_model("news", "NewsBlock")
        for block in block_class.objects.all():
            block.content = block.description
            block.save()

    dependencies = [
        ('news', '0003_auto_20141115_2358'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
