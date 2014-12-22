import re
from statuses.models import STATUSES, Status

__author__ = 'eraldo'


class ManagerCommandParser():
    """
    Used to find out if a given string is a project or task.
    Can return the found task/project data.
    """
    @property
    def _project(self):
        return r"^(?P<project>!{status}:(\s+)?{name}(\s+)?)$".format(
            status=self._status,
            name=self._name)

    @property
    def _task(self):
        return r"^(?P<task>{status}:(\s+)?{name}(\s+)?)$".format(
            status=self._status,
            name=self._name
        )

    @property
    def _status(self):
        return r"(?P<status>{status_options})".format(
            status_options=self._status_options
        )

    @property
    def _status_options(self):
        options = self._status_map.keys()
        return r"({})".format("|".join(options))

    @property
    def _name(self):
        return r"(?P<name>.*)"

    def __init__(self, string):
        self.string = string
        self._status_map = self._generate_statuses_dict()

    @staticmethod
    def _generate_statuses_dict():
        statuses = STATUSES

        status_map = {}

        # All capital status words
        all_capital_statuses = {state: state.lower() for state in statuses}
        status_map.update(all_capital_statuses)

        # First Letter status words
        first_letter_statuses = {state[0]: state.lower() for state in statuses}
        status_map.update(first_letter_statuses)

        return status_map

    def _get_data(self, pattern):
        matches = re.match(pattern, self.string)
        if matches:
            return matches.groupdict()

    @property
    def is_project(self):
        return bool(self._get_data(self._project))

    @property
    def project_data(self):
        return self._get_data(self._project)

    @property
    def is_task(self):
        return bool(self._get_data(self._task))

    @property
    def task_data(self):
        return self._get_data(self._task)

    def _update_status(self, data):
        if not data:
            return
        status = data.get("status")
        if status:
            status = self._status_map.get(status)
            data["status"] = Status.objects.get(name=status)
        return data

    def parse(self):
        data = {}
        if self.is_project:
            data = self._get_data(self._project)
        elif self.is_task:
            data = self._get_data(self._task)
        if data:
            data = self._update_status(data)
        return data
