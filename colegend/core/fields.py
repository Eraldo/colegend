from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db import models
from simplemde.fields import SimpleMDEField


class MarkdownField(SimpleMDEField):
    pass


class DateFieldWidget(forms.DateInput):
    input_type = 'date'


class DateTimeFieldWidget(DateFieldWidget):
    format = "YYYY-MM-DD HH:mm"


class TimeFieldWidget(DateFieldWidget):
    format = "HH:mm"


class DateFormField(forms.DateField):
    widget = DateFieldWidget


class DateTimeFormField(forms.DateField):
    widget = DateTimeFieldWidget


class TimeFormField(forms.DateField):
    widget = TimeFieldWidget


class DateField(models.DateField):
    def formfield(self, **kwargs):
        defaults = {'form_class': DateFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class DateTimeField(models.DateTimeField):
    def formfield(self, **kwargs):
        defaults = {'form_class': DateTimeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class TimeField(models.TimeField):
    def formfield(self, **kwargs):
        defaults = {'form_class': TimeFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
