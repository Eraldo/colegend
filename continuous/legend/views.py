from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class Chapter1View(LoginRequiredMixin, TemplateView):
    template_name = "legend/chapter1.html"
