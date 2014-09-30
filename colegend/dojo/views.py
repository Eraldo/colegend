from django.views.generic import TemplateView
from lib.views import ActiveUserRequiredMixin

__author__ = 'eraldo'


class DojoMixin(ActiveUserRequiredMixin):
    pass


class DojoView(DojoMixin, TemplateView):
    template_name = "dojo/dojo.html"
