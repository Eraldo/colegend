from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, RedirectView

from colegend.core.views import RolesRequiredMixin
from .forms import CategoryForm
from .models import Category


class CategoryMixin(object):
    """
    Default attributes and methods for category related views.
    """
    model = Category
    form_class = CategoryForm


class CategoryIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'categories:list'


class CategoryListView(LoginRequiredMixin, CategoryMixin, ListView):
    template_name = 'categories/list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, RolesRequiredMixin, CategoryMixin, CreateView):
    template_name = 'categories/create.html'
    required_roles = ['admin']


class CategoryDetailView(LoginRequiredMixin, CategoryMixin, DetailView):
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        number = category.order
        animals = {
            1: {
                'name': 'bear',
                'favorites': [
                    ('Topics', ''),
                    ('Color', ''),
                    ('Body Part', ''),
                    ('Chakra', ''),
                ],
                'story': '',
            },
            2: {
                'name': 'dolphin',
                'favorites': [
                    ('Topics', ''),
                    ('Color', ''),
                    ('Body Part', ''),
                    ('Chakra', ''),
                ],
                'story': '',
            },
            3: {
                'name': 'tiger',
                'favorites': [
                    ('Topics', ''),
                    ('Color', ''),
                    ('Body Part', ''),
                    ('Chakra', ''),
                ],
                'story': '',
            },
            4: {
                'name': 'monkey',
                'favorites': [
                    ('Topics', ''),
                    ('Color', ''),
                    ('Body Part', ''),
                    ('Chakra', ''),
                ],
                'story': '',
            },
            5: {
                'name': 'parrot',
                'favorites': [
                    ('Topics', ''),
                    ('Color', ''),
                    ('Body Part', ''),
                    ('Chakra', ''),
                ],
                'story': '',
            },
            6: {
                'name': 'eagle',
                'favorites': [
                    ('Topics', ''),
                    ('Color', ''),
                    ('Body Part', ''),
                    ('Chakra', ''),
                ],
                'story': '',
            },
            7: {
                'name': 'phoenix',
                'favorites': [
                    ('Topics', 'spiritual & purpose'),
                    ('Color', 'violet'),
                    ('Body Part', 'energy field'),
                    ('Chakra', 'crown chakra'),
                ],
                'story': 'adsfsdf',
            },
        }
        context['animal'] = animals.get(number)
        return context


class CategoryUpdateView(LoginRequiredMixin, RolesRequiredMixin, CategoryMixin, UpdateView):
    template_name = 'categories/update.html'
    required_roles = ['admin']


class CategoryDeleteView(LoginRequiredMixin, RolesRequiredMixin, CategoryMixin, DeleteView):
    template_name = 'categories/delete.html'
    required_roles = ['admin']

    def get_success_url(self):
        return reverse('categories:index')
