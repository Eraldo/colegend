from django.views.generic import TemplateView


class AcademyView(TemplateView):
    template_name = "about/academy.html"
