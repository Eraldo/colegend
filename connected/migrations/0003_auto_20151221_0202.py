# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('connected', '0002_connected_virtual_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='connected',
            name='chat_introduction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='connected',
            name='guide_introduction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='connected',
            name='guidelines_introduction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='connected',
            name='virtual_room_introduction',
            field=models.BooleanField(default=False),
        ),
    ]
