# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('continuous', '0005_auto_20160102_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continuous',
            old_name='diary',
            new_name='pioneer_journal',
        ),
        migrations.RenameField(
            model_name='continuous',
            old_name='journal',
            new_name='your_journal',
        ),
    ]
