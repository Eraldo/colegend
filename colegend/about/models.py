from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models

# Create your models here.
from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page


class AboutPage(Page):
    def serve(self, request, *args, **kwargs):
        return redirect('about')
