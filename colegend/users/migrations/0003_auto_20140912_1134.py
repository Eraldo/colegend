# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lib.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20140912_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male Legend ♂'), ('F', 'Female Legend ♀')])),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', lib.modelfields.PhoneField(help_text='Mobile or other phone number. Example: +4369910203039', max_length=16)),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='street',
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.OneToOneField(null=True, to='users.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(null=True, to='users.Profile'),
            preserve_default=True,
        ),
    ]
