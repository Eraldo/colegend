# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields
import phonenumber_field.modelfields
import django.contrib.auth.models
import django.core.validators
import core.utils.media_paths
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status',
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     default=False)),
                ('username', models.CharField(verbose_name='username',
                                              error_messages={'unique': 'A user with that username already exists.'},
                                              validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                                                                'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
                                                                                                'invalid')],
                                              max_length=30, unique=True,
                                              help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status',
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 default=False)),
                ('is_active', models.BooleanField(verbose_name='active',
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('name', models.CharField(verbose_name='name', help_text='Your full name', max_length=255)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neutral')])),
                ('birthday', models.DateField(null=True, blank=True)),
                ('address', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('occupation', models.CharField(verbose_name='occupation(s)', max_length=255, blank=True)),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(
                    upload_to=core.utils.media_paths.UploadToOwnedDirectory('avatars'))),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', blank=True,
                                                  related_query_name='user',
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  to='auth.Group')),
                ('user_permissions',
                 models.ManyToManyField(verbose_name='user permissions', related_name='user_set', blank=True,
                                        related_query_name='user', help_text='Specific permissions for this user.',
                                        to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'legends',
                'verbose_name': 'legend',
                'default_related_name': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
