from django.db import models

# Create your models here.
from django.shortcuts import redirect
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from colegend.cms.models import UniquePageMixin


class HomePage(UniquePageMixin, Page):
    template = 'home/index.html'

    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full")
    ]

    def serve(self, request, *args, **kwargs):
        user = request.user
        # Redirect anonymous users to the about page.
        if not user.is_authenticated():
            return redirect("about")
        # Redirect if prologue is not completed.
        if not user.has_checkpoint('prologue'):
            return redirect("story:prologue")
        return super().serve(request, *args, **kwargs)

    def __str__(self):
        return self.title
