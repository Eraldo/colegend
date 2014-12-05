from django.template.loader import render_to_string
from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from tutorials.models import get_tutorial
from visions.forms import VisionForm
from visions.models import Vision


__author__ = 'eraldo'


class VisionMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Vision
    form_class = VisionForm
    icon = "vision"

    def form_valid(self, form):
        try:
            return super(VisionMixin, self).form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super(VisionMixin, self).form_invalid(form)


class VisionListView(VisionMixin, ListView):
    def get(self, request, *args, **kwargs):
        # redirect the user to his vision or create a new one
        try:
            vision = request.user.vision
        except Vision.DoesNotExist:
            vision = None
        if vision:
            return redirect(vision)
        else:
            return redirect("visions:vision_new")


class VisionNewView(VisionMixin, CreateView):
    success_url = reverse_lazy('visions:vision_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(VisionNewView, self).form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        template = render_to_string("visions/vision.md")
        initial['content'] = template
        return initial


class VisionShowView(VisionMixin, DetailView):
    template_name = "visions/vision_show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutorial'] = get_tutorial("Life Vision")
        return context


class VisionEditView(VisionMixin, UpdateView):
    success_url = reverse_lazy('visions:vision_list')


class VisionDeleteView(VisionMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('visions:vision_list')
