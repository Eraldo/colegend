# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cards.models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20150216_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=cards.models.get_deck_upload_path)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(to='cards.Deck', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='text',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to=cards.models.get_card_upload_path),
            preserve_default=True,
        ),
    ]
