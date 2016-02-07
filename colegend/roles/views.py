from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, RedirectView

from colegend.core.views import OwnedCreateView, OwnedUpdateView, OwnedItemsMixin
from .models import Role
from .forms import RoleForm


class RoleMixin(OwnedItemsMixin):
    """
    Default attributes and methods for Role related views.
    """
    model = Role
    form_class = RoleForm


class RoleIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'roles:list'


class RoleListView(LoginRequiredMixin, RoleMixin, ListView):
    template_name = 'roles/list.html'
    context_object_name = 'roles'


class RoleCreateView(LoginRequiredMixin, RoleMixin, OwnedCreateView):
    template_name = 'roles/create.html'


class RoleDetailView(LoginRequiredMixin, RoleMixin, DetailView):
    template_name = 'roles/detail.html'


class RoleUpdateView(LoginRequiredMixin, RoleMixin, OwnedUpdateView):
    template_name = 'roles/update.html'
    context_object_name = 'object'


class RoleDeleteView(LoginRequiredMixin, RoleMixin, DeleteView):
    template_name = 'roles/delete.html'

    def get_success_url(self):
        role = self.get_object()
        return role.index_url()
