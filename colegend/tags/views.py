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
        return tag.index_url()


class TagAutocompleteView(LoginRequiredMixin, TagMixin, Select2QuerySetView):
    """
    A django view providing autocomplete data.
    """
    # def get_queryset(self):
    #     user = self.request.user
    #     # Don't forget to filter out results depending on the visitor !
    #     if not user.is_authenticated():
    #         return Tag.objects.none()
    #
    #     qs = Tag.objects.owned_by(user)
    #     if self.q:
    #         qs = qs.filter(name__icontains=self.q)
    #
    #     return self.q
