from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, 'home.html', {'notes': notes})

def navbar(request):
    return HttpResponse("<h1>Hello Vasu Successfully Done</h1>")
