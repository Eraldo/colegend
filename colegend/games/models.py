# from django.core.urlresolvers import reverse
# from django.db import models
#
# from colegend.core.models import AutoOwnedBase
# from colegend.categories.models import Category
#
#
# class Game(AutoOwnedBase):
#     hand = models.ManyToManyField(Card, related_name='games_hand', blank=True)
#     completed = models.ManyToManyField(Card, related_name='games_completed', blank=True)
#
#     # checkpoints = models.ManyToManyField(Checkpoint, related_name='games', blank=True)
#
#     @property
#     def deck(self):
#         completed = [card.id for card in self.completed.all()]
#         hand = [card.id for card in self.hand.all()]
#         excluded = completed + hand
#         return Card.objects.exclude(id__in=excluded)
#
#     @property
#     def can_draw(self):
#         """
#         Checks:
#         1. there is room in the hand
#         2. there is a card in the deck
#         :return:
#         """
#         hand = self.hand
#         deck = self.deck
#         if hand.count() >= 1:
#             return False
#         if not deck.count():
#             return False
#         return True
#
#     def draw(self):
#         if not self.can_draw:
#             return False
#         card = self.deck.first()
#         self.hand.add(card)
#         return card
#
#     def get_card(self, name):
#         try:
#             return Card.objects.get(name__iexact=name)
#         except Card.DoesNotExist:
#             return False
#
#     def has_card(self, card):
#         if isinstance(card, str):
#             card = self.get_card(card)
#         if card in self.completed.all():
#             return True
#         if card in self.hand.all():
#             return True
#         return False
#
#     def complete_card(self, card):
#         if isinstance(card, str):
#             card = self.get_card(card)
#         if card in self.hand.all():
#             self.hand.remove(card)
#             self.completed.add(card)
#             self.save()
#             return True
#         return False
#
#     @property
#     def last_completed_card(self):
#         return self.completed.last()
#
#     def __str__(self):
#         return "{}'s tutorial game".format(self.owner)
#
#     @staticmethod
#     def get_absolute_url():
#         return reverse('games:index')
