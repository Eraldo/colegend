import re
from django.utils import timezone
from statuses.models import STATUSES, Status
from tags.models import Tag

__author__ = 'eraldo'


class ManagerCommandParser():
    """
    Used to find out if a given string is a project or task.
    Can return the found task/project data.
    """

    @property
    def _project(self):
        return r"^(?P<project>!{status}:(\s+)?{name}(\s+)?{context}(\s+)?)$".format(
            status=self._status,
            name=self._name,
            context=self._context,
        )

    @property
    def _task(self):
        return r"^(?P<task>{status}:(\s+)?{name}(\s+)?{context}(\s+)?)$".format(
            status=self._status,
            name=self._name,
            context=self._context,
        )

    @property
    def _context(self):
        return r"{date}(\s+)?{deadline}(\s+)?{tags}".format(
            date=self._date,
            deadline=self._deadline,
            tags=self._tags,
        )

    @property
    def _date(self):
        # TODO: update to accept only valid numbers (e.g. month `14`)
        return r"(>(?P<date>\d{4}-\d{2}-\d{2}))?"

    @property
    def _deadline(self):
        return r"(!(?P<deadline>\d{4}-\d{2}-\d{2}))?"

    @property
    def _tags(self):
        return r"(\[(?P<tags>.*?)\])?"

    @property
    def _tag(self):
        return r"^(?P<tag>TAG:(\s+)?{name}(\s+)?)$".format(
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
        return r"(?P<name>.*?)"

    def __init__(self, string, user):
        self.string = string
        self.user = user
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
            data = matches.groupdict()
            return dict((key, value) for key, value in data.items() if value)

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

    @property
    def is_tag(self):
        return bool(self._get_data(self._tag))

    @property
    def tag_data(self):
        return self._get_data(self._tag)

    def _update_status(self, data):
        if not data:
            return
        status = data.get("status")
        if status:
            status = self._status_map.get(status)
            data["status"] = Status.objects.get(name=status)
        return data

    def _update_tags(self, data):
        if not data:
            return
        if not data.get('tags'):
            return data
        tags_string = data.get("tags")
        tags = []
        tags_list = tags_string.split(",")
        user = self.user
        for tag_string in tags_list:
            tag_string = tag_string.strip()
            try:
                tag = user.tags.get(name=tag_string)
                tags.append(tag)
            except Tag.DoesNotExist:
                raise ValueError("Tag: '{}' does not exist.".format(tag_string))
        data.pop("tags")
        if tags:
            data["tags"] = tags
        return data

    @staticmethod
    def _update_date(data):
        if not data:
            return
        date_string = data.get('date')
        if not date_string:
            return data
        try:
            date = timezone.datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Date: '{}' could not be interpreted.".format(date_string))
        data["date"] = date
        return data

    @staticmethod
    def _update_deadline(data):
        if not data:
            return
        deadline_string = data.get('deadline')
        if not deadline_string:
            return data
        try:
            deadline = timezone.datetime.strptime(deadline_string, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Deadline: '{}' could not be interpreted.".format(deadline_string))
        data["deadline"] = deadline
        return data

    def parse(self):
        data = {}
        if self.is_project:
            data = self._get_data(self._project)
            if data.get("date"):
                data.pop("date")
        elif self.is_task:
            data = self._get_data(self._task)
        elif self.is_tag:
            data = self._get_data(self._tag)
        if data:
            data = self._update_status(data)
            data = self._update_date(data)
            data = self._update_deadline(data)
            data = self._update_tags(data)
        return data
