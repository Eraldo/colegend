from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, Submit, Div
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django.core.urlresolvers import reverse_lazy
from floppyforms.__future__.models import ModelForm
import floppyforms as forms
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from lib.formfields import PhoneField
from lib.validators import PhoneValidator, validate_date_in_past
from users.models import User, Profile, Settings

__author__ = 'eraldo'


class UserForm(ModelForm):
    class Meta:
        # Set this form to use the User model.
        model = User
        # Constrain the UserForm to just these fields.
        fields = ["username"]

    helper = FormHelper()
    helper.form_action = reverse_lazy("users:update")
    helper.layout = Layout(
        Field('username', autofocus='True'),
        SaveButton(),
        CancelButton(),
    )


class UserCreationForm(AuthUserCreationForm):
    """
    Custom user creation form.
    """
    username = forms.CharField(max_length=30)

    class Meta(AuthUserCreationForm.Meta):
        model = User

    def clean_username(self):
        """
        Custom username clean method overwrite.

        This is used because django's default implementation hardcodes the auth.user.

        :return: :raise forms.ValidationError:
        """
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User


class SignUpApplicationForm(ModelForm):
    # CONTACT FIELDS
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male Legend ♂'),
        ('F', 'Female Legend ♀'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    birthday = forms.DateField(validators=[validate_date_in_past])
    email = forms.EmailField()
    phone_number = PhoneField(help_text="Mobile or other phone number. Example: +4369910203039")
    street = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=5)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = [
            'origin', "referrer", 'experience', 'motivation', 'change', 'drive', 'expectations', 'other',
            'stop', 'discretion', 'responsibility', 'appreciation', 'terms',
        ]

    def __init__(self, *args, **kwargs):
        initial = kwargs.get("initial")
        if initial:  # should exist
            username = initial.get("username")
            first_name = initial.get("first_name")
            kwargs["initial"]["first_name"] = first_name or username
        super(SignUpApplicationForm, self).__init__(*args, **kwargs)
        # remove some labels
        if self.fields.get('referrer'):
            self.fields['referrer'].label = ""
        if self.fields.get('username'):
            self.fields['username'].label = ""

    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            "Introduction",
            HTML("""Welcome"""),
            Field("username"),
            HTML("""{% include 'users/_introduction.html' %}""")
        ),
        Fieldset(
            "Questions",
            "origin",
            Field("referrer", placeholder="Contact Person"),
            "experience",
            "motivation",
            "change",
            Field("drive", type="range", min=1, max=10),
            Field("foo", type="range", min=1, max=10),
            "expectations",
            "other"
        ),
        Fieldset(
            "Guidelines",
            HTML("""<label>I accept the following guidelines:</label>"""),
            Field("stop", required=True),
            Field("discretion", required=True),
            Field("responsibility", required=True),
            Field("appreciation", required=True),
            Field("terms", required=True),
        ),
        Fieldset(
            "Contact",
            Div(
                Field("first_name", wrapper_class="col-md-6"),
                Field("last_name", wrapper_class="col-md-6"),
                css_class="row",
            ),
            Div(
                Field("gender", wrapper_class="col-md-6"),
                Field("birthday", wrapper_class="col-md-6"),
                css_class="row",
            ),
            Div(
                Field("email", wrapper_class="col-md-6"),
                Field("phone_number", pattern=PhoneValidator.regex, title=PhoneValidator.message,
                      wrapper_class="col-md-6"),
                css_class="row",
            ),
            Div(
                Field("street", wrapper_class="col-md-6"),
                Field("postal_code", wrapper_class="col-md-2"),
                Field("city", wrapper_class="col-md-2"),
                Field("country", wrapper_class="col-md-2"),
                css_class="row",
            ),
            Div(
                Field("", wrapper_class="col-md-6"),
                css_class="row",
            ),
            Div(
                Field("", wrapper_class="col-md-6"),
            ),
        ),
        Fieldset(
            "{% if form.fields.password1 %}Account{% endif %}",
            Field("password1", wrapper_class="col-md-6"),
            Field("password2", wrapper_class="col-md-6"),
            "confirmation_key",
            css_class="row",
        ),
        HTML(
            """<hr>If you are happy with your answers..<br>
            feel free to go ahead and send the application form.<br>I'll see you on the other side. ;)</p>"""),
        HTML("""
            {% if redirect_field_value %}
                <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}"/>
            {% endif %}
        """)
    )
    helper.add_input(Submit('save', 'Send Application'))
    helper.form_tag = False

    def signup(self, request, user):
        pass


class SettingsForm(ModelForm):
    class Meta:
        model = Settings
        fields = ['language', 'day_start', 'keyboard', 'sound', 'journal_entry_template']
        widgets = {
            'journal_entry_template': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            "General Settings",
            Field("language"),
            Field("day_start"),
            Field("keyboard"),
            # TODO: Fix workaround (Is there another way to add a help text?)
            HTML("""
                <a id="hint_id_keyboard" href="{% url "tutorials:keyboard" %}"
                target="_blank" class="help-block" style="position: relative; top: -15px;">
                {% load icons %}{% icon "tutorial" %} Keyboard Tutorial</a>"""),
            Field("sound"),
        ),
        Fieldset(
            "Journal Settings",
            Field("journal_entry_template"),
        ),
        SaveButton(),
    )
