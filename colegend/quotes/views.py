from django.views.generic import TemplateView
from lib.views import ActiveUserRequiredMixin
from quotes.models import Quote


class QuoteMixin(ActiveUserRequiredMixin):
    model = Quote


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
