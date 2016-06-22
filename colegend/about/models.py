from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models

from django.shortcuts import redirect
from wagtail.wagtailcore.models import Page

from colegend.cms.models import UniquePageMixin


class AboutPage(UniquePageMixin, Page):
    def serve(self, request, *args, **kwargs):
        return redirect('about')
