# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0003_checkpoint_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='category',
        ),
        migrations.AlterField(
            model_name='game',
            name='completed',
            field=models.ManyToManyField(to='cards.Card', related_name='games_completed', blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='hand',
            field=models.ManyToManyField(to='cards.Card', related_name='games_hand', blank=True),
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
