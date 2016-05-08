from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request):
    todos = Todo.objects.order_by('created_date')
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    if request.method == "TODO":
        form = TodoForm(data=request.TODO)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.projectname = request
            todo.description = request
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_list', pk=todo.pk)
    else:
        form = TodoForm()
        context = {'form': form, 'create': True}
        return render(request, 'newtodo.html', context)

def edit_todo(request):
    todos = Todo.objects.order_by('created_date')
    return render(request, 'edittodo.html', {'todos': todos})

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(instance=todo, data=request.TODO)
        if form.is_valid():
            form.save()
            return redirect('edittodo.html')
    else:
        form = TodoForm(instance=todo)
    context = {'form': form, 'create': False}
    return render(request, 'edittodo.html', context)

def impressum(request):
    return render(request, 'impressum.html', {})


