# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('innercall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innercall',
            name='other',
            field=models.TextField(blank=True, verbose_name='Is there anything else you want to share? :)'),
        ),
        migrations.AlterField(
            model_name='innercall',
            name='wishes',
            field=models.TextField(blank=True, verbose_name='What are your wishes for this platform?'),
        ),
    ]
