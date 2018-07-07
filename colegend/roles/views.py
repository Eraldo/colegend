from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView
from rest_framework import viewsets

from colegend.core.views import RolesRequiredMixin
from .models import Role
from .forms import RoleForm
from .serializers import RoleSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_queryset(self):
        user = self.request.user
        return user.roles.all()


class RoleMixin(object):
    """
    Default attributes and methods for role related views.
    """
    model = Role
    form_class = RoleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['manager'] = self.request.user.has_role(name='Secretary')
        return context


class RoleIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'roles:list'


class RoleListView(RoleMixin, ListView):
    template_name = 'roles/list.html'
    context_object_name = 'roles'


class RoleCreateView(LoginRequiredMixin, RolesRequiredMixin, RoleMixin, CreateView):
    template_name = 'roles/create.html'
    required_roles = ['Secretary']

    def get_initial(self):
        initial = super().get_initial()
        return initial


class RoleDetailView(RoleMixin, DetailView):
    template_name = 'roles/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['energizers'] = self.get_object().users.all()
        return context


class RoleUpdateView(LoginRequiredMixin, RolesRequiredMixin, RoleMixin, UpdateView):
    template_name = 'roles/update.html'
    required_roles = ['Secretary']


class RoleDeleteView(LoginRequiredMixin, RolesRequiredMixin, RoleMixin, DeleteView):
    template_name = 'roles/delete.html'
    required_roles = ['Secretary']

    def get_success_url(self):
        role = self.get_object()
        return role.index_url
