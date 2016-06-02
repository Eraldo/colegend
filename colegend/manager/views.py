from django.shortcuts import render

# Create your views here.
from django.views.generic import RedirectView


class ManagerIndexView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'outcomes:list'
