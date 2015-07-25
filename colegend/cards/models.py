import os
from django.db import models
from lib.models import AutoUrlMixin

__author__ = 'eraldo'


def get_deck_upload_path(instance, filename):
    return os.path.join("cards", str(instance.name), filename)


class Deck(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=get_deck_upload_path)

    def __str__(self):
        return self.name

    @property
    def shuffled_cards(self):
        return self.cards.order_by('?')


def get_card_upload_path(instance, filename):
    return os.path.join("cards", str(instance.deck), filename)


class Card(AutoUrlMixin, models.Model):
    deck = models.ForeignKey(Deck, related_name="cards", related_query_name="card")
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=get_card_upload_path)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
