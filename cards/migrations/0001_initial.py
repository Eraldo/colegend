# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0004_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('sort_order', models.IntegerField(blank=True, db_index=True)),
                ('image', models.ImageField(upload_to='game/cards/', blank=True)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('details', models.TextField(blank=True)),
                ('category', models.ManyToManyField(to='categories.Category', related_name='cards')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
