from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from projects.models import Project


class ProjectListView(ListView):
    model = Project