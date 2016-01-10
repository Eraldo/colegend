# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('image', models.ImageField(upload_to='games/cards/', blank=True)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('details', models.TextField(blank=True)),
                ('category', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
