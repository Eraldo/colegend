from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit, HTML, Button
from django import forms
from django.core.mail import EmailMessage
from lib.crispy import IconButton

__author__ = 'Eraldo Helal'


class ContactForm(forms.Form):
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def send_email(self, user):
        # send email using the self.cleaned_data dictionary
        email = user.email
        subject = "[CoLegend] Message from '{}'".format(user)
        message = self.cleaned_data["message"]
        email = EmailMessage(subject, message, email, ['connect@colegend.org'], headers={'Reply-To': email})
        email.send()

    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Contact Form',
            Field('message', rows="4", css_class='form-control', placeholder="Your message...",
                  style="resize: vertical;", autofocus="True"),
        ),
        IconButton("send", "Send", "send", input_type="submit", css_class="btn-primary")
    )


class PublicContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def send_email(self, user=None):  # User should be anonymous user.
        # send email using the self.cleaned_data dictionary
        email = self.cleaned_data["email"]
        subject = "[CoLegend] Message from '{}'".format(email)
        message = self.cleaned_data["message"]
        email = EmailMessage(subject, message, email, ['connect@colegend.org'], headers={'Reply-To': email})
        email.send()

    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Contact Form',
            Field('email', placeholder="Your email address..."),
            Field('message', rows="4", css_class='form-control', placeholder="Your message...",
                  style="resize: vertical;", autofocus="True"),
        ),
        IconButton("send", "Send", "send", input_type="submit", css_class="btn-primary")
    )
