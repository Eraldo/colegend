from lib.views import ActiveUserRequiredMixin, get_icon
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from tags.forms import TagForm
from tags.models import Tag
from tutorials.models import get_tutorial


__author__ = 'eraldo'


class TagMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Tag
    form_class = TagForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["icon"] = get_icon("tag")
        return context

    def form_valid(self, form):
        try:
            return super(TagMixin, self).form_valid(form)
        except ValidationError as e:
            # Catch model errors (e.g. unique_together).
            form.add_error(None, e)
            return super(TagMixin, self).form_invalid(form)


class TagListView(TagMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tutorial'] = get_tutorial("Tags")
        return context


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

    def get_context_data(self, **kwargs):
        context = super(TagEditView, self).get_context_data(**kwargs)
        # The context variable 'tag' conflicts with the crispy form template
        # which also uses the variable 'tag' to insert 'html-div-tags'.
        context.pop('tag')
        return context


class TagDeleteView(TagMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('tags:tag_list')
