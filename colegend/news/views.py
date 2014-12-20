from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from news.forms import NewsBlockForm
from news.models import NewsBlock
from lib.views import ManagerRequiredMixin, ActiveUserRequiredMixin

__author__ = 'eraldo'


class NewsBlockMixin():
    model = NewsBlock
    form_class = NewsBlockForm
    icon = "news"


class NewsBlockListView(ActiveUserRequiredMixin, NewsBlockMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        return context


class NewsBlockCreateView(ManagerRequiredMixin, NewsBlockMixin, CreateView):
    success_url = reverse_lazy('news:newsblock_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class NewsBlockShowView(ActiveUserRequiredMixin, NewsBlockMixin, DetailView):
    template_name = "news/newsblock_show.html"


class NewsBlockEditView(ManagerRequiredMixin, NewsBlockMixin, UpdateView):
    pass


class NewsBlockDeleteView(ManagerRequiredMixin, NewsBlockMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('news:newsblock_list')
