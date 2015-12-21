# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from .models import User


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/legend.html'

    # TODO: Write custom get_object method
    # redirecting if no slug is given and otherwise using the slug


class SettingsView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/settings.html'

    def get_object(self, queryset=None):
        return self.request.user


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("home")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['first_name', 'last_name']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("legends:profile",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserIntroductionView(LoginRequiredMixin, TemplateView):
    template_name = 'users/introduction.html'

    def post(self, request, *args, **kwargs):
        if 'success' in request.POST:
            # update connected path
            user = request.user
            user.connected.legend_introduction = True
            user.connected.save()
            # redirect to profile
            return redirect('legends:profile', user.username)
        return self.get(request, *args, **kwargs)
