from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import SaveButton, CancelButton
from tags.models import Tag
from trackers.models import Weight, Sex, Book, Joke, Transaction, Dream

__author__ = 'eraldo'


class WeightForm(ModelForm):
    class Meta:
        model = Weight
        fields = ['time', 'weight', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('time'),
        Field('weight', autofocus='True'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class SexForm(ModelForm):
    class Meta:
        model = Sex
        fields = ['date', 'amount', 'person', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Row(
            Field('amount', autofocus='True', wrapper_class="col-md-6"),
            Field('person', wrapper_class="col-md-6"),
        ),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'status', 'url', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('title', autofocus='True', wrapper_class="col-md-6"),
            Field('author', wrapper_class="col-md-6"),
        ),
        Row(
            Field('status', wrapper_class="col-md-6"),
            Field('url', wrapper_class="col-md-6"),
        ),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['name', 'description', 'notes', 'rating']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Field('notes', rows=2),
        Field('rating'),
        SaveButton(),
        CancelButton(),
    )


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['time', 'amount', 'transaction_type', 'description', 'category', 'tags', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('time'),
        Row(
            Field('amount', autofocus='True', wrapper_class="col-md-6"),
            Field('transaction_type', wrapper_class="col-md-6"),
        ),
        Field('description', rows=2),
        Row(
            Field('category', wrapper_class="col-md-6"),
            Field('tags', wrapper_class="col-md-6"),
        ),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class DreamForm(ModelForm):
    class Meta:
        model = Dream
        fields = ['date', 'name', 'description', 'symbols']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('name', autofocus='True'),
        Field('description'),
        Field('symbols'),
        SaveButton(),
        CancelButton(),
    )
