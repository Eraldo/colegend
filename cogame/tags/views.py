from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from tags.models import Tag


__author__ = 'eraldo'


class TagMixin(LoginRequiredMixin, OwnedItemsMixin):
    model = Tag
    fields = ['name', 'description']


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
