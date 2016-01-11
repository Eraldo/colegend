from django.core.urlresolvers import reverse
from django.db import models
from orderable.models import Orderable
from categories.models import Category


class Card(Orderable):
    image = models.ImageField(upload_to='games/cards/', blank=True)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    details = models.TextField(blank=True)
    category = models.ManyToManyField(Category, related_name="cards")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cards:detail', kwargs={'pk': self.pk})
