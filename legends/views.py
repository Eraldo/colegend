from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, ListView
from django.utils.translation import ugettext as _

from games.views import complete_card
from users.models import User
from .models import Legend
from .forms import LegendForm, BiographyForm, AvatarForm


class LegendDetailView(LoginRequiredMixin, DetailView):
    template_name = 'legends/detail.html'
    model = Legend

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['can_edit_about'] = user.game.has_card('about')
        context['outercall'] = user.game.has_card('outer call')
        context['innercall'] = user.game.has_card('inner call')
        context['biography'] = user.game.has_card('biography')
        return context

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

    def get(self, request, *args, **kwargs):
        user = request.user
        connected = user.connected
        if connected.about or user.game.has_card('about'):
            return super().get(request, *args, **kwargs)
        else:
            messages.warning(request, 'You need to unlock this feature first.')
            return redirect('games:index')

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            user = User.objects.get(username=owner)
        else:
            user = self.request.user
        return user.legend

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

    def form_valid(self, form):
        request = self.request
        connected = request.user.connected
        if not connected.about:
            connected.about = True
            connected.save()
            # update game
            complete_card(request, 'about')
        else:
            message = _('changes saved')
            messages.success(self.request, message)
        return super().form_valid(form)


class LegendAvatarView(LegendUpdateView):
    template_name = 'legends/avatar.html'
    form_class = AvatarForm


class LegendListView(LoginRequiredMixin, ListView):
    template_name = 'legends/list.html'
    model = Legend
    context_object_name = 'legends'


class BiographyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'legends/biography.html'
    model = Legend
    form_class = BiographyForm

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            user = User.objects.get(username=owner)
        else:
            user = self.request.user
        return user.legend

    def form_valid(self, form):
        request = self.request
        connected = request.user.connected
        if not connected.biography:
            connected.biography = True
            connected.save()
            # update game
            complete_card(request, 'biography')
        else:
            message = _('changes saved')
            messages.success(self.request, message)
        return super().form_valid(form)
