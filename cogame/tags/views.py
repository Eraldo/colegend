from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tags.models import Tag


__author__ = 'eraldo'


class TagMixin(LoginRequiredMixin):
    model = Tag


class TagListView(TagMixin, ListView):
    pass


class TagNewView(TagMixin, CreateView):
    success_url = reverse_lazy('tags:tag_list')


class TagShowView(TagMixin, DetailView):
    template_name = "tags/tag_show.html"


class TagEditView(TagMixin, UpdateView):
    success_url = reverse_lazy('tags:tag_list')


class TagDeleteView(TagMixin, DeleteView):
    success_url = reverse_lazy('tags:tag_list')