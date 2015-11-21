# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import environ
from django.db import migrations


class Migration(migrations.Migration):
    def add_social_apps(apps, schema_editor):
        """
        Create initial social apps for facebook and google.
        Keys are taken from the environment.
        :param schema_editor:
        :return:
        """
        Site = apps.get_model("sites", "Site")
        site = Site.objects.first()
        SocialApp = apps.get_model("socialaccount", "SocialApp")
        env = environ.Env()

        # Google app
        google_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id='862909939438.apps.googleusercontent.com',
            secret=env("GOOGLE_KEY", default='insert your key here')
        )
        site.socialapp_set.add(google_app)

        # Facebook app
        facebook_app = SocialApp.objects.create(
            provider='facebook',
            name='Facebook',
            client_id='173658052814028',
            secret=env("FACEBOOK_KEY", default='insert your key here')
        )
        site.socialapp_set.add(facebook_app)

    dependencies = [
        ('sites', '0001_initial'),
        ('socialaccount', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_social_apps),
    ]
