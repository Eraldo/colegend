from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView
from dojo.forms import ModuleForm
from dojo.models import Module
from lib.views import ActiveUserRequiredMixin

__author__ = 'eraldo'


class DojoMixin(ActiveUserRequiredMixin):
    model = Module
    form_class = ModuleForm


class DojoView(DojoMixin, TemplateView):
    template_name = "dojo/dojo.html"

    def get_context_data(self, **kwargs):
        context = super(DojoView, self).get_context_data(**kwargs)
        context['modules'] = Module.objects.filter(accepted=True)
        return context


class ModuleCreateView(DojoMixin, CreateView):
    success_url = reverse_lazy('dojo:home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.provider = user
        return super(ModuleCreateView, self).form_valid(form)


class ModuleShowView(DojoMixin, DetailView):
    template_name = "dojo/module_show.html"
