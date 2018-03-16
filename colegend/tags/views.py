from dal.autocomplete import Select2QuerySetView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, RedirectView

from colegend.core.views import OwnedCreateView, OwnedUpdateView, OwnedItemsMixin
from .models import Tag
from .forms import TagForm


class TagMixin(OwnedItemsMixin):
    """
    Default attributes and methods for Tag related views.
    """
    model = Tag
    form_class = TagForm


class TagIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'tags:list'


class TagListView(LoginRequiredMixin, TagMixin, ListView):
    template_name = 'tags/list.html'
    context_object_name = 'tags'


class TagCreateView(LoginRequiredMixin, TagMixin, OwnedCreateView):
    template_name = 'tags/create.html'


class TagDetailView(LoginRequiredMixin, TagMixin, DetailView):
    template_name = 'tags/detail.html'


class TagUpdateView(LoginRequiredMixin, TagMixin, OwnedUpdateView):
    template_name = 'tags/update.html'
    context_object_name = 'object'


class TagDeleteView(LoginRequiredMixin, TagMixin, DeleteView):
    template_name = 'tags/delete.html'

    def get_success_url(self):
        tag = self.get_object()
        return tag.index_url


class TagAutocompleteView(LoginRequiredMixin, TagMixin, Select2QuerySetView):
    """
    A django view providing autocomplete data.
    """
    create_field = 'name'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.owned_by(user)

    def create_object(self, text):
        """Create an object given a text."""
        owner = self.request.user
        return self.get_queryset().create(**{self.create_field: text}, owner=owner)

    def has_add_permission(self, request):
        """Return True if the user has the permission to add a model."""
        if not request.user.is_authenticated:
            return False
        return True
