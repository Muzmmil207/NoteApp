from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CreateNote
# Create your views here.

class NotesListView(ListView):
    template_name = 'homepage.html'
    model = CreateNote