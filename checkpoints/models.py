# from django.db import models
#
# from core.models import OwnedBase, TimeStampedBase
#
#
# class CheckpointName(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Checkpoint(OwnedBase, TimeStampedBase):
#
#     name = models.ForeignKey(CheckpointName)
#
#     class Meta:
#         default_related_name = 'checkpoints'
#
#     def __str__(self):
#         return self.name
