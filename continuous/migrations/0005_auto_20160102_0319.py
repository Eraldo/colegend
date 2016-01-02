# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('continuous', '0004_auto_20160102_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='continuous',
            old_name='dear_diary',
            new_name='diary',
        ),
        migrations.RenameField(
            model_name='continuous',
            old_name='the_journal',
            new_name='journal',
        ),
        migrations.RenameField(
            model_name='continuous',
            old_name='entering_leyenda',
            new_name='leyenda',
        ),
    ]
