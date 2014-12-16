# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20141211_1935'),
        ('journals', '0009_remove_dayentry_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('owner', annoying.fields.AutoOneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dayentry',
            name='journal',
            field=models.ForeignKey(default=1, related_name='entries', to='journals.Journal'),
            preserve_default=False,
        ),
    ]
