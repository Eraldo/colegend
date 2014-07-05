from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tags.models import Tag


__author__ = 'eraldo'


class TagListView(ListView):
    model = Tag


class TagNewView(CreateView):
    model = Tag
    success_url = reverse_lazy('tags:tag_list')


class TagShowView(DetailView):
    model = Tag
    template_name = "tags/tag_show.html"


class TagEditView(UpdateView):
    model = Tag
    success_url = reverse_lazy('tags:tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags:tag_list')