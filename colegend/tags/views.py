from braces.views import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from tags.forms import TagForm
from tags.models import Tag


__author__ = 'eraldo'


class TagMixin(LoginRequiredMixin, OwnedItemsMixin):
    model = Tag
    form_class = TagForm

    def form_valid(self, form):
        try:
            return super(TagMixin, self).form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super(TagMixin, self).form_invalid(form)


class TagListView(TagMixin, ListView):
    pass


class TagNewView(TagMixin, CreateView):
    success_url = reverse_lazy('tags:tag_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(TagNewView, self).form_valid(form)


class TagShowView(TagMixin, DetailView):
    template_name = "tags/tag_show.html"


class TagEditView(TagMixin, UpdateView):
    success_url = reverse_lazy('tags:tag_list')


class TagDeleteView(TagMixin, DeleteView):
    success_url = reverse_lazy('tags:tag_list')
