from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Fieldset, Submit
from django import forms
from django.core.mail import send_mail

__author__ = 'Eraldo Helal'


class ContactForm(forms.Form):
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def send_email(self, user):
        # send email using the self.cleaned_data dictionary
        subject = "[CoLegend] Message from '{}'".format(user)
        message = self.cleaned_data["message"]
        send_mail(subject, message, user.email, ['eraldo@colegend.org'])

    helper = FormHelper()
    helper.add_input(Submit('send', 'Send'))
    helper.layout = Layout(
        Fieldset(
            'Contact Form',
            Field('message', rows="4", css_class='form-control', placeholder="Your message...",
                  style="resize: vertical;", autofocus="True"),
        ),
        # HTML("""
        # <br>
        # <button type="submit" class="btn btn-lg btn-primary"><span class="glyphicon glyphicon-send"></span> send
        # message
        # </button>
        #  """),
    )
