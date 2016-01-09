from django.db import models
from orderable.models import Orderable
from categories.models import Category
from core.models import AutoOwnedBase
from cards.models import Card


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
        completed = [card.id for card in self.completed.all()]
        hand = [card.id for card in self.hand.all()]
        excluded = completed + hand
        return Card.objects.exclude(id__in=excluded)

    @property
    def can_draw(self):
        """
        Checks:
        1. there is room in the hand
        2. there is a card in the deck
        :return:
        """
        hand = self.hand
        deck = self.deck
        if hand.count() >= 3:
            return False
        if not deck.count():
            return False
        return True

    def draw(self):
        if not self.can_draw:
            return False
        card = self.deck.first()
        self.hand.add(card)
        return card

    def __str__(self):
        return "{}'s game".format(self.owner)
