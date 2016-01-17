from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView, ListView
from django.utils.translation import ugettext as _

from games.views import complete_card
from users.forms import LegendForm, AvatarForm
from users.models import User
from .models import Profile
from .forms import BiographyForm


# class ProfileDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'profiles/detail.html'
#     model = Profile
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         context['can_edit_about'] = user.game.has_card('about')
#         context['outercall'] = user.game.has_card('outer call')
#         context['innercall'] = user.game.has_card('inner call')
#         context['biography'] = user.game.has_card('biography')
#         return context
#
#     def get_object(self, queryset=None):
#         owner = self.kwargs.get('owner')
#         if owner:
#             user = User.objects.get(username=owner)
#         else:
#             user = self.request.user
#         return user.profile


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'profiles/update.html'
#     model = Profile
#     form_class = LegendForm
#
#     def get(self, request, *args, **kwargs):
#         user = request.user
#         connected = user.connected
#         if connected.about or user.game.has_card('about'):
#             return super().get(request, *args, **kwargs)
#         else:
#             messages.warning(request, 'You need to unlock this feature first.')
#             return redirect('games:index')
#
#     def get_object(self, queryset=None):
#         owner = self.kwargs.get('owner')
#         if owner:
#             user = User.objects.get(username=owner)
#         else:
#             user = self.request.user
#         return user.profile
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         fields = self.request.GET.get('fields')
#         if fields:
#             kwargs['fields'] = fields
#         return kwargs
#
#     def get_initial(self):
#         initial = super().get_initial()
#         profile = self.get_object()
#         name = profile.name
#         if not name:
#             initial['name'] = profile.owner.get_full_name()
#         return initial
#
#     def form_valid(self, form):
#         request = self.request
#         connected = request.user.connected
#         if not connected.about:
#             connected.about = True
#             connected.save()
#             # update game
#             complete_card(request, 'about')
#         else:
#             message = _('changes saved')
#             messages.success(self.request, message)
#         return super().form_valid(form)


# class ProfileListView(LoginRequiredMixin, ListView):
#     template_name = 'profiles/list.html'
#     model = Profile
#     context_object_name = 'profiles'


class BiographyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/biography.html'
    model = Profile
    form_class = BiographyForm

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if owner:
            user = User.objects.get(username=owner)
        else:
            user = self.request.user
        return user.profile

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
