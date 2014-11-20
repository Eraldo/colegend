from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit
from django import forms
from django.core.mail import send_mail, EmailMessage

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
    helper.add_input(Submit('send', 'Send'))
    helper.layout = Layout(
        Fieldset(
            'Contact Form',
            Field('message', rows="4", css_class='form-control', placeholder="Your message...",
                  style="resize: vertical;", autofocus="True"),
        ),
    )


class PublicContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def send_email(self, user):
        # send email using the self.cleaned_data dictionary
        email = self.cleaned_data["email"]
        subject = "[CoLegend] Message from '{}'".format(email)
        message = self.cleaned_data["message"]
        email = EmailMessage(subject, message, email, ['connect@colegend.org'], headers={'Reply-To': email})
        email.send()

    helper = FormHelper()
    helper.add_input(Submit('send', 'Send'))
    helper.layout = Layout(
        Fieldset(
            'Contact Form',
            Field('email', placeholder="Your email address..."),
            Field('message', rows="4", css_class='form-control', placeholder="Your message...",
                  style="resize: vertical;", autofocus="True"),
        ),
    )
