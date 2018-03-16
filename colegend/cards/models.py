# from django.urls import reverse
# from django.db import models
# from easy_thumbnails.fields import ThumbnailerImageField
# from colegend.categories.models import Category
#
#
# class Card(Orderable):
#     image = ThumbnailerImageField(
#         upload_to='games/cards/',
#         blank=True,
#         resize_source=dict(size=(250, 250)),
#     )
#     name = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     details = models.TextField(blank=True)
#     category = models.ManyToManyField(Category, related_name="cards")
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('cards:detail', kwargs={'pk': self.pk})
#
#     @property
#     def update_url(self):
#         return reverse('cards:update', kwargs={'pk': self.pk})
#
#     @property
#     def delete_url(self):
#         return reverse('cards:delete', kwargs={'pk': self.pk})
