from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from dojo.forms import ModuleForm
from dojo.models import Module
from lib.views import ActiveUserRequiredMixin

__author__ = 'eraldo'


class DojoMixin(ActiveUserRequiredMixin):
    model = Module
    form_class = ModuleForm
    icon = "dojo"
    tutorial = "Dojo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DojoView(DojoMixin, TemplateView):
    template_name = "dojo/dojo.html"

    def get_context_data(self, **kwargs):
        context = super(DojoView, self).get_context_data(**kwargs)
        context['modules'] = Module.objects.filter(accepted=True)
        context["contribution_counter"] = Module.objects.filter(provider=self.request.user).count()
        return context


class ModuleCreateView(DojoMixin, CreateView):
    success_url = reverse_lazy('dojo:home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.provider = user
        return super(ModuleCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        template = render_to_string("dojo/module.md")
        initial['content'] = template
        return initial


class ModuleShowView(DojoMixin, DetailView):
    template_name = "dojo/module_show.html"


class ModuleEditView(DojoMixin, UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user == self.get_object().provider:
            return super(ModuleEditView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class ModuleDeleteView(DojoMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('dojo:home')
