from django.shortcuts import redirect
from django.views.generic import TemplateView


class SupportView(TemplateView):
    template_name = 'support/index.html'


class FAQView(TemplateView):
    template_name = 'support/faq.html'


class DocumentationView(TemplateView):
    template_name = 'support/documentation.html'
