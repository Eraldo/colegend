from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import OwnedCreateView, OwnedUpdateView, OwnedItemsMixin
from .models import Vision
from .forms import VisionForm


class VisionMixin(OwnedItemsMixin):
    """
    Default attributes and methods for vision related views.
    """
    model = Vision
    form_class = VisionForm


class VisionIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'visions:list'


class VisionListView(LoginRequiredMixin, VisionMixin, ListView):
    template_name = 'visions/list.html'
    context_object_name = 'visions'


class VisionCreateView(LoginRequiredMixin, VisionMixin, OwnedCreateView):
    template_name = 'visions/create.html'


class VisionDetailView(LoginRequiredMixin, VisionMixin, DetailView):
    template_name = 'visions/detail.html'


class VisionUpdateView(LoginRequiredMixin, VisionMixin, OwnedUpdateView):
    template_name = 'visions/update.html'


class VisionDeleteView(LoginRequiredMixin, VisionMixin, DeleteView):
    template_name = 'visions/delete.html'

    def get_success_url(self):
        vision = self.get_object()
        return vision.index_url
