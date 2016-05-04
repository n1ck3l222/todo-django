from django.shortcuts import render
from django.utils import timezone
from .models import Todo

# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(name='ralf').order_by('created_date')
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    return render(request, 'newtodo.html', {})

def edit_todo(request):
    return render(request, 'edittodo.html')

