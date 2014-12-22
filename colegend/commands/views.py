import re
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import redirect, render
from statuses.models import Status
from tutorials.models import get_tutorial

__author__ = 'eraldo'


def _handle_command(request, command):
    # help
    if command in ["help", "h", "--h", "--help", "?"]:
        message = get_tutorial("Quick Commands").description
        messages.add_message(request, messages.INFO, message)
        return
    # clear
    if command == "clear":
        return
    # task
    task_pattern = r'^(?P<status>TODO|DONE):(\s+)?(?P<name>.*)$'
    task_match = re.match(task_pattern, command)
    if task_match:
        task_data = task_match.groupdict()
        task_data["status"] = Status.objects.get(name=task_data["status"].lower())
        try:
            task = request.user.tasks.create(**task_data)
        except ValidationError as e:
            message = "Error: {}".format(e.messages[0])
            messages.add_message(request, messages.ERROR, message)
            return
        if task.status.name == "todo":
            status = ''
        else:
            status = '({})'.format(task.status)
        message = "Created Task: '{name}' {status}".format(status=status, name=task.name)
        messages.add_message(request, messages.SUCCESS, message)
        return

    # command not found
    message = "Unknown command: '{}'.".format(command)
    messages.add_message(request, messages.SUCCESS, message)


def quick_command(request):
    # prepare
    command = request.POST.get("command")

    # act
    if command:
        _handle_command(request, command)

    if request.is_ajax():
        return render(request, "website/_messages.html")

    # redirect
    next_url = request.POST.get('next')
    if next_url:
        return redirect(next_url)
    return Http404
