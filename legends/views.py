from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView
from django.utils.translation import ugettext as _

from users.models import User
from .models import Legend
from .forms import LegendForm, BiographyForm, AvatarForm, MeForm


class LegendDetailView(LoginRequiredMixin, DetailView):
    template_name = 'legends/detail.html'
    model = Legend

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            user = User.objects.get(username=owner)
        else:
            user = self.request.user
        return user.legend


class LegendUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'legends/update.html'
    model = Legend
    form_class = LegendForm

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            return Legend.objects.get(owner__username=owner)
        else:
            return self.request.user.legend

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        fields = self.request.GET.get('fields')
        if fields:
            kwargs['fields'] = fields
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        legend = self.get_object()
        name = legend.name
        if not name:
            initial['name'] = legend.owner.get_full_name()
        return initial


class LegendAvatarView(LegendUpdateView):
    template_name = 'legends/avatar.html'
    form_class = AvatarForm


class LegendListView(LoginRequiredMixin, ListView):
    template_name = 'legends/list.html'
    model = Legend
    context_object_name = 'legends'


class MeUpdateView(LegendUpdateView):
    template_name = 'legends/me.html'
    form_class = MeForm

    def form_valid(self, form):
        connected = self.get_object().owner.connected
        if not connected.me:
            connected.me = True
            connected.save()
            message = _('biography completed')
            messages.success(self.request, message)
        else:
            message = _('changes saved')
            messages.success(self.request, message)
        return super().form_valid(form)


class BiographyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'legends/biography.html'
    model = Legend
    form_class = BiographyForm

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            return Legend.objects.get(owner__username=owner)
        else:
            return self.request.user.legend

    def form_valid(self, form):
        message = _('changes saved')
        messages.success(self.request, message)
        return super().form_valid(form)
