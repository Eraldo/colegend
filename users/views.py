# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, ListView

from games.views import complete_card
from users.forms import AvatarForm, LegendForm
from .models import User
from django.utils.translation import ugettext as _


# class ProfileView(LoginRequiredMixin, DetailView):
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#     template_name = 'users/profile.html'
#
#     def get_object(self, queryset=None):
#         username = self.kwargs.get('username')
#         if username:
#             return super().get_object(queryset)
#         else:
#             return self.request.user


class SettingsView(LoginRequiredMixin, DetailView):
    template_name = 'users/settings.html'
    model = User

    def get_object(self, queryset=None):
        return self.request.user


# class UserUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'users/update.html'
#     fields = ['first_name', 'last_name']
#
#     # we already imported User in the view code above, remember?
#     model = User
#
#     # send the user back to their own page after a successful update
#     def get_success_url(self):
#         return reverse("legends:profile",
#                        kwargs={"username": self.request.user.username})
#
#     def get_object(self):
#         # Only get the User record for the user making the request
#         return User.objects.get(username=self.request.user.username)


# class UserListView(LoginRequiredMixin, ListView):
#     template_name = 'users/list.html'
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = "username"
#     slug_url_kwarg = "username"


# class UserIntroductionView(LoginRequiredMixin, TemplateView):
#     template_name = 'users/introduction.html'
#
#     def post(self, request, *args, **kwargs):
#         if 'success' in request.POST:
#             # update connected path
#             user = request.user
#             user.connected.legend_introduction = True
#             user.connected.save()
#             # redirect to profile
#             return redirect('legends:profile', user.username)
#         return self.get(request, *args, **kwargs)

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
        context['can_edit_about'] = user.game.has_card('about')
        context['outercall'] = user.game.has_card('outer call')
        context['innercall'] = user.game.has_card('inner call')
        context['biography'] = user.game.has_card('biography')
        return context


class LegendUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'legends/update.html'
    model = User
    form_class = LegendForm
    context_object_name = 'legend'

    def get(self, request, *args, **kwargs):
        user = request.user
        connected = user.connected
        if connected.about or user.game.has_card('about'):
            return super().get(request, *args, **kwargs)
        else:
            messages.warning(request, 'You need to unlock this feature first.')
            return redirect('games:index')

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


class LegendAvatarView(LegendUpdateView):
    template_name = 'profiles/avatar.html'
    form_class = AvatarForm

    def get(self, request, *args, **kwargs):
        user = request.user
        connected = user.connected
        if connected.avatar or user.game.has_card('profile picture'):
            return super().get(request, *args, **kwargs)
        else:
            messages.warning(request, 'You need to unlock this feature first.')
            return redirect('games:index')

    def get_initial(self):
        # overwriting the LegendUpdateView method
        return super().get_initial()

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
