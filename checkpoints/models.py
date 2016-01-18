from django.db import models


class Checkpoint(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        default_related_name = 'checkpoints'

    def __str__(self):
        return self.name
