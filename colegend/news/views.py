from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from news.forms import NewsBlockForm
from news.models import NewsBlock
from lib.views import ManagerRequiredMixin, ActiveUserRequiredMixin

__author__ = 'eraldo'


class NewsBlockMixin(ManagerRequiredMixin):
    model = NewsBlock
    form_class = NewsBlockForm


class NewsBlockListView(ActiveUserRequiredMixin, ListView):
    model = NewsBlock


class NewsBlockCreateView(NewsBlockMixin, CreateView):
    success_url = reverse_lazy('news:newsblock_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class NewsBlockShowView(ActiveUserRequiredMixin, DetailView):
    model = NewsBlock
    template_name = "news/newsblock_show.html"


class NewsBlockEditView(NewsBlockMixin, UpdateView):
    pass


class NewsBlockDeleteView(NewsBlockMixin, DeleteView):
    success_url = reverse_lazy('news:newsblock_list')
