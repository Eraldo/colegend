# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20140912_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='appreciation',
            field=users.modelfields.RequiredBooleanField(default=False, help_text='I am willing to treat the Platform and its members with appreciation.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='change',
            field=models.TextField(default='-', help_text='Possible topics could be: home, relationships, work, purpose, self, etc.', verbose_name='What do you want to change in your life?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='discretion',
            field=users.modelfields.RequiredBooleanField(default=False, help_text='Everything stays in the CoLegend World.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='drive',
            field=models.PositiveIntegerField(default=10, help_text='1 = very low, 10 = very high', verbose_name='How strong is your drive/willingness to change yourself to get there?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='expectations',
            field=models.TextField(default='-', help_text='What do you think or wish the platform can do for you?', verbose_name='What are your expectations of this platform?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.TextField(default='-', help_text='Seminars? Workshops? Education? Books? etc', verbose_name='Do you have prior Personal Development Experience?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='motivation',
            field=models.TextField(default='-', verbose_name='What is your motivation to join this platform?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='origin',
            field=models.TextField(default='-', help_text='Talking with someone? Internet search? Other source/medium?', verbose_name='How did you get to know CoLegend?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='other',
            field=models.TextField(blank=True, null=True, verbose_name='Anything else you want to share?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='referrer',
            field=models.CharField(blank=True, max_length=30, null=True, help_text='If a person introduced you to CoLegend.. please mention his/her/their name here.', verbose_name='Contact Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='responsibility',
            field=users.modelfields.RequiredBooleanField(default=False, help_text='I am responsible for my own experience.', verbose_name='Individual Responsibility'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='stop',
            field=users.modelfields.RequiredBooleanField(default=False, help_text="When someone says 'stop' it means stop!", verbose_name='Stop Rule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='terms',
            field=users.modelfields.RequiredBooleanField(default=False, help_text='I accept the general advice, terms and conditions.', verbose_name='Terms and Conditions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_tester',
            field=models.BooleanField(default=False, help_text="Designates whether the user can access the site's test features.", verbose_name='tester status'),
        ),
    ]
