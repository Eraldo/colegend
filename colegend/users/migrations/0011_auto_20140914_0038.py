# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20140913_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_accepted',
            field=models.BooleanField(help_text='Designates whether the user has been accepted by the site managers.', verbose_name='accepted', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_tester',
            field=models.BooleanField(help_text="Designates whether the user can access the site's test features.", verbose_name='tester', default=False),
        ),
    ]
