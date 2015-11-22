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
        if not site:
            site = Site.objects.create(domain='localhost:8000', name='localhost')
        SocialApp = apps.get_model("socialaccount", "SocialApp")
        env = environ.Env()

        # Google app
        google_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id=env("GOOGLE_ID"),
            secret=env("GOOGLE_KEY")
        )
        # print(site, google_app)
        site.socialapp_set.add(google_app)

        # Facebook app
        facebook_app = SocialApp.objects.create(
            provider='facebook',
            name='Facebook',
            client_id=env("FACEBOOK_ID"),
            secret=env("FACEBOOK_KEY")
        )
        site.socialapp_set.add(facebook_app)
        print(facebook_app.secret)

    dependencies = [
        ('sites', '0001_initial'),
        ('socialaccount', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_social_apps),
    ]
