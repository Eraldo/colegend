from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from manager.parser import ManagerCommandParser
from tutorials.models import get_tutorial

__author__ = 'eraldo'


def _handle_command(request, command):
    # help
    if command in ["help", "--help", "?"]:
        message = get_tutorial("Quick Commands").description
        messages.add_message(request, messages.INFO, message)
        return

    # clear
    if command in ["clear", "-"]:
        return

    parser = ManagerCommandParser(command, request.user)
    try:
        data = parser.parse()
    except ValueError as error:
        messages.add_message(request, messages.WARNING, mark_safe(str(error)))
        return
    # task
    if "task" in data:
        data.pop("task")
        try:
            tags = data.get("tags")
            if tags:
                data.pop("tags")
            task = request.user.tasks.create(**data)
            if tags:
                task.tags.add(*tags)
                task.save()
        except ValidationError as e:
            message = "Error: {}".format(e.messages[0])
            messages.add_message(request, messages.ERROR, message)
            return
        message = "Created Task: '{name}'".format(
            name=render_to_string("tasks/_task_link.html", {"task": task}))
        messages.add_message(request, messages.SUCCESS, mark_safe(message))
        return

    # project
    if "project" in data:
        data.pop("project")
        try:
            tags = data.get("tags")
            if tags:
                data.pop("tags")
            project = request.user.projects.create(**data)
            if tags:
                project.tags.add(*tags)
                project.save()
        except ValidationError as e:
            message = "Error: {}".format(e.messages[0])
            messages.add_message(request, messages.ERROR, message)
            return
        message = "Created Project: '{name}'".format(
            name=render_to_string("projects/_project_link.html", {"project": project}))
        messages.add_message(request, messages.SUCCESS, mark_safe(message))
        return

    # tag
    if "tag" in data:
        data.pop("tag")
        try:
            tag = request.user.tags.create(**data)
        except ValidationError as e:
            message = "Error: {}".format(e.messages[0])
            messages.add_message(request, messages.ERROR, message)
            return
        message = "Created Tag: '{name}'".format(
            name=render_to_string("tags/_tag.html", {"tag": tag}))
        messages.add_message(request, messages.SUCCESS, mark_safe(message))
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
