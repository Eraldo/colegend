from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db import models
from simplemde.fields import SimpleMDEField


class MarkdownField(SimpleMDEField):
    pass


class DateFieldWidget(DateTimePicker):
    format = "YYYY-MM-DD"
    icons = {
        'time': 'fa fa-clock-o',
        'date': 'fa fa-calendar',
        'up': 'fa fa-chevron-up',
        'down': 'fa fa-chevron-down',
        'previous': 'fa fa-chevron-left',
        'next': 'fa fa-chevron-right',
        'today': 'fa fa-crosshairs',
        'clear': 'fa fa-trash',
        'close': 'fa fa-times'
    }

    def __init__(self, attrs=None, format=None, options=None, div_attrs=None, icon_attrs=None):
        options = options or {"format": self.format, 'icons': self.icons, 'locale': 'en-gb'}
        icon_attrs = icon_attrs or {'class': 'fa fa-calendar'}
        super().__init__(attrs, format, options, div_attrs, icon_attrs)

    js_template = """
    <script>
      window.onload = function(){
        $("#%(picker_id)s:has(input:not([readonly],[disabled]))").datetimepicker(%(options)s);
      };
    </script>"""

    html_template = """
    <div%(div_attrs)s>
      <span class="input-group-addon">
        <span%(icon_attrs)s></span>
      </span>
      <input%(input_attrs)s/>
    </div>"""

    class Media:
        css = {
            'all': (
                'components/eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.min.css',
            )
        }
        js = (
            'components/moment/min/moment-with-locales.min.js',
            'components/eonasdan-bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js',
        )


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
