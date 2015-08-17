from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, HTML, Div
from django.forms import ModelForm
from lib.crispy import SaveButton, CancelButton
from trackers.models import Weight, Sex, Book, Joke, Transaction, Dream, Sleep, Walk, \
    Tracker, CheckData, NumberData, RatingData

__author__ = 'eraldo'


class CheckDataForm(ModelForm):
    class Meta:
        model = CheckData
        fields = ['date', 'notes']
    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('notes', placeholder="Notes"),
        HTML("""<input type="hidden" name="data-type" value="Check">"""),
        HTML("""{% load icons %}<button type="submit" class="btn btn-default">{% icon "check" %}</button>"""),
    )
    helper.form_class = "form-inline"
    helper.form_show_labels = False
    error_text_inline = False


class NumberDataForm(ModelForm):
    class Meta:
        model = NumberData
        fields = ['date', 'number', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('number', placeholder="Number", autofocus='True'),
        Field('notes', placeholder="Notes"),
        HTML("""<input type="hidden" name="data-type" value="Number">"""),
        HTML("""{% load icons %}<button type="submit" class="btn btn-default">{% icon "check" %}</button>"""),
    )
    helper.form_class = "form-inline"
    helper.form_show_labels = False


class RatingDataForm(ModelForm):
    class Meta:
        model = RatingData
        fields = ['date', 'rating', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('rating', placeholder="1-5", autofocus='True'),
        Field('notes', placeholder="Notes"),
        HTML("""<input type="hidden" name="data-type" value="Rating">"""),
        HTML("""{% load icons %}<button type="submit" class="btn btn-default">{% icon "check" %}</button>"""),
    )
    helper.form_class = "form-inline"
    helper.form_show_labels = False


class TrackerForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ['name', 'description', 'category', 'tracker_type', 'frequency', 'chart_type']

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Div(
                Field('name', autofocus='True'),
                Field('description', rows=2),
                css_class="col-md-6"
            ),
            Field('category', wrapper_class="col-md-3"),
            Field('tracker_type', wrapper_class="col-md-3"),
            Field('frequency', wrapper_class="col-md-3"),
            Field('chart_type', wrapper_class="col-md-3"),
        ),
        SaveButton(),
        CancelButton(),
    )


class WeightForm(ModelForm):
    class Meta:
        model = Weight
        fields = ['time', 'weight', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('time'),
        AppendedText('weight', 'kg', autofocus='True', help_text=''),
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
        fields = ['title', 'author', 'status', 'category', 'book_type',
                  'start_date', 'end_date', 'origin', 'feedback', 'rating', 'url', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('title', autofocus='True', wrapper_class="col-md-8"),
            Field('author', wrapper_class="col-md-4"),
        ),
        Row(
            Field('book_type', wrapper_class="col-md-3"),
            Field('category', wrapper_class="col-md-3"),
            Field('status', wrapper_class="col-md-2"),
            Field('start_date', wrapper_class="col-md-2"),
            Field('end_date', wrapper_class="col-md-2"),
        ),
        Row(
            Field('url', wrapper_class="col-md-6"),
            Field('origin', wrapper_class="col-md-3"),
            Field('rating', wrapper_class="col-md-3"),
            ),
        Row(
            Field('notes', wrapper_class="col-md-6"),
            Field('feedback', wrapper_class="col-md-6"),
        ),
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


class SleepForm(ModelForm):
    class Meta:
        model = Sleep
        fields = ['start', 'end', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('start', autofocus='True'),
        Field('end'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )


class WalkForm(ModelForm):
    class Meta:
        model = Walk
        fields = ['start', 'end', 'notes']

    helper = FormHelper()
    helper.layout = Layout(
        Field('start', autofocus='True'),
        Field('end'),
        Field('notes', rows=2),
        SaveButton(),
        CancelButton(),
    )
