from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tags.models import Tag


__author__ = 'eraldo'


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    success_url = reverse_lazy('tags:list')


class TagDetailView(DetailView):
    model = Tag


class TagUpdateView(UpdateView):
    model = Tag
    success_url = reverse_lazy('tags:list')


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags:list')