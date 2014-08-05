from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import FormView
from commands.forms import CommandsForm

__author__ = 'eraldo'


def process_command(command, request):
    message = ""
    command = command.strip()

    if command.startswith("help"):
        message = "Please contact us for help."
    elif command.startswith("+p: "):
        project_name = command.split()
        message = "TODO: created project '{}'.".format(command[4:])

    if message:
        messages.add_message(request, messages.INFO, message)


class CommandsView(LoginRequiredMixin, FormView):
    template_name = "commands/commands.html"
    form_class = CommandsForm
    success_url = "."

    def form_valid(self, form):
        request = self.request
        command = form.cleaned_data['command']
        process_command(command, request)
        return super(CommandsView, self).form_valid(form)
