from crispy_forms.layout import Field


class IconField(Field):
    icon = ''
    template = 'bootstrap3/iconfield.html'

    def __init__(self, field, icon, *args, **kwargs):
        self.icon = icon
        super().__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, extra_context=None, **kwargs):
        if extra_context is None:
            extra_context = {}
        icon = self.icon
        if icon:
            extra_context['icon'] = icon
        return super().render(form, form_style, context, extra_context=extra_context, **kwargs)
