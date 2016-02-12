from dal.fields import CreateModelMultipleField
from dal_select2.widgets import ModelSelect2Multiple


class TagsCreateFormField(CreateModelMultipleField):
    widget = ModelSelect2Multiple(url='tags:autocomplete')

    def create_value(self, value):
        owner = self.owner
        return self.queryset.model.objects.create(name=value, owner=owner).pk

    def __init__(self, queryset, owner, required=True, widget=None, label=None,
                 initial=None, help_text='', *args, **kwargs):
        self.owner = owner
        super().__init__(queryset, required, widget, label,
                 initial, help_text, *args, **kwargs)
