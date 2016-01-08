from django.db import models
from orderable.models import Orderable
from categories.models import Category


class Card(Orderable):
    image = models.ImageField(upload_to='game/cards/', blank=True)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    details = models.TextField(blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
