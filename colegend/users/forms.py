from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field, Submit
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from floppyforms.__future__.models import ModelForm
import floppyforms as forms
from lib.formfields import PhoneField
from lib.validators import validate_in_past, PhoneValidator
from users.models import User, Profile, Contact

__author__ = 'eraldo'


class UserForm(ModelForm):
    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ["username"]


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
    birthday = forms.DateField(validators=[validate_in_past])
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
        super(SignUpApplicationForm, self).__init__(*args, **kwargs)
        self.fields['referrer'].label = ""
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
            "first_name",
            "last_name",
            "gender",
            "birthday",
            "email",
            Field("phone_number", pattern=PhoneValidator.regex, title=PhoneValidator.message),
            "street",
            "postal_code",
            "city",
            "country",
        ),
        Fieldset(
            "{% if form.fields.password1 %}Account{% endif %}",
            # HTML("""{% if form.fields.password1 %}Account{% endif %}"""),
            # "Account",
            "password1",
            "password2",
            "confirmation_key"
        ),
        HTML(
            """<hr>If you are happy with your answers..<br>
            feel free to go ahead and send the application form.</p>"""),
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
