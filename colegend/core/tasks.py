# Create your tasks here
from celery import shared_task
from django.core import management


@shared_task
def add(x, y):
    return x + y


@shared_task
def call_command(command_name, *args, **kwargs):
    management.call_command(command_name, *args, **kwargs)
