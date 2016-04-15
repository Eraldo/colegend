# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, UpdateView, ListView
from django.utils.translation import ugettext as _

from colegend.core.views import CheckpointsRequiredMixin
from colegend.games.views import complete_card
from colegend.users.forms import AvatarForm, LegendForm

from .models import User


class SettingsView(LoginRequiredMixin, DetailView):
    template_name = 'users/settings.html'
    model = User

    def get_object(self, queryset=None):
        return self.request.user


class LegendListView(LoginRequiredMixin, ListView):
    template_name = 'legends/list.html'
    model = User
    context_object_name = 'legends'


class LegendDetailView(LoginRequiredMixin, DetailView):
    template_name = 'legends/detail.html'
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'legend'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        legend = self.get_object()
        if user == legend:
            page_links = [
                {
                    'name': 'Outer Call',
                    'url': reverse('outer-call:create'),
                    'locked': not user.has_checkpoint('outer call card')
                },
                {
                    'name': 'Inner Call',
                    'url': reverse('inner-call:create'),
                    'locked': not user.has_checkpoint('inner call card')
                },
                {
                    'name': 'Biography',
                    'url': reverse('biography:create'),
                    'locked': not user.has_checkpoint('biography card')
                },
                {
                    'name': 'About',
                    'url': reverse('legends:update', kwargs={'username': legend.username}),
                    'locked': not user.has_checkpoint('about card')
                },
            ]
            # update the kind and id
            kind = 'link btn-sm'
            for link in page_links:
                name = link.get('name')
                slug = slugify(name)
                id = '{}-button'.format(slug)
                link.update({'kind': kind, 'id': id})
            context['page_links'] = page_links
        context['core_manager'] = legend.has_role('core manager')
        context['cloud_guide'] = legend.has_role('guide')
        context['roles'] = legend.roles.all()
        return context


class LegendUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'legends/update.html'
    model = User
    form_class = LegendForm
    context_object_name = 'legend'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.has_checkpoint('about card'):
            return super().get(request, *args, **kwargs)
        else:
            game_url = user.game.get_absolute_url()
            game_link = '<a href="{}">game</a>'.format(game_url)
            message = _('You need to unlock this feature in the {}.').format(game_link)
            messages.warning(request, mark_safe(message))
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        if username:
            user = User.objects.get(username=username)
        else:
            user = self.request.user
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        fields = self.request.GET.get('fields')
        if fields:
            kwargs['fields'] = fields
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        user = self.get_object()
        name = user.name
        if not name:
            initial['name'] = user.get_full_name()
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


class LegendAvatarView(LoginRequiredMixin, CheckpointsRequiredMixin, UpdateView):
    template_name = 'legends/avatar.html'
    model = User
    form_class = AvatarForm
    context_object_name = 'legend'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    required_checkpoints = ['profile picture card']

    def form_valid(self, form):
        request = self.request
        connected = request.user.connected
        if not connected.avatar:
            connected.avatar = True
            connected.save()
            # update game
            complete_card(request, 'profile picture')
        else:
            message = _('changes saved')
            messages.success(self.request, message)
        return super().form_valid(form)
