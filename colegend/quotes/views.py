from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView
from lib.views import ActiveUserRequiredMixin
from quotes.forms import QuoteForm
from quotes.models import Quote


class QuoteMixin(ActiveUserRequiredMixin):
    model = Quote
    form_class = QuoteForm


class RandomQuoteView(QuoteMixin, TemplateView):
    template_name = "quotes/random.html"

    def get_context_data(self, **kwargs):
        context = super(RandomQuoteView, self).get_context_data(**kwargs)
        try:
            quote = Quote.objects.order_by('?').first()
        except Quote.DoesNotExist:
            quote = None
        context['quote'] = quote
        return context


class QuoteCreateView(QuoteMixin, CreateView):
    success_url = reverse_lazy('quotes:random')

    def form_valid(self, form):
        user = self.request.user
        form.instance.provider = user
        return super(QuoteCreateView, self).form_valid(form)
