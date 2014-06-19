from django import forms

__author__ = 'eraldo'


class CommandsForm(forms.Form):
    command = forms.CharField()