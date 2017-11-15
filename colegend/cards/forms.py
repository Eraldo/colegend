# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit
# from django import forms
#
# from .models import Card
#
# __author__ = 'Eraldo Energy'
#
#
# class CardForm(forms.ModelForm):
#     class Meta:
#         model = Card
#         fields = [
#             'name',
#             'image',
#             'content',
#             'details',
#             'category',
#         ]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             'name',
#             'image',
#             'content',
#             'details',
#             'category',
#         )
#         self.helper.add_input(Submit('save', 'Save'))
