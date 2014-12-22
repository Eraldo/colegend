from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect

__author__ = 'eraldo'


def quick_command(request):
    # prepare
    command = request.POST.get("command")
    # act
    if command:
        message="Sent command: '{}'.".format(command)
        messages.add_message(request, messages.SUCCESS, message)
    # redirect
    next_url = request.POST.get('next')
    if next_url:
        return redirect(next_url)
    return Http404
