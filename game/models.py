from django.db import models
from orderable.models import Orderable
from categories.models import Category
from core.models import AutoOwnedBase


class Card(Orderable):
    image = models.ImageField(upload_to='game/cards/', blank=True)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    details = models.TextField(blank=True)
    category = models.ManyToManyField(Category, related_name="cards")

    def __str__(self):
        return self.name


class Checkpoint(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(AutoOwnedBase):
    hand = models.ManyToManyField(Card, related_name='games_hand', blank=True)
    completed = models.ManyToManyField(Card, related_name='games_completed', blank=True)
    checkpoints = models.ManyToManyField(Checkpoint, blank=True)

    @property
    def deck(self):
        return Card.objects.exclude(id__in=[self.completed, self.hand])

    def __str__(self):
        return "{}'s game".format(self.owner)
