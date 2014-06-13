from django.db import models


class Project(models.Model):
    """
    A django model representing a project.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    history = models.TextField(blank=True)

    def __str__(self):
        return self.name