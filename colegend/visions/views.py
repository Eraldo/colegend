from lib.views import ActiveUserRequiredMixin
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from visions.forms import VisionForm
from visions.models import Vision


__author__ = 'eraldo'


class VisionMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Vision
    form_class = VisionForm

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


class VisionShowView(VisionMixin, DetailView):
    template_name = "visions/vision_show.html"


class VisionEditView(VisionMixin, UpdateView):
    success_url = reverse_lazy('visions:vision_list')


class VisionDeleteView(VisionMixin, DeleteView):
    success_url = reverse_lazy('visions:vision_list')
