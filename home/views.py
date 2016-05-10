from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import UpdateView

from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request):
    todos = Todo.objects.order_by('created_date')
    return render(request, 'index.html', {'todos': todos})

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_date = timezone.now()
            todo.save()
            todos = Todo.objects.order_by('created_date')
            return render(request, 'index.html', {'todos': todos})
    else:
        form = TodoForm()
        context = {'form': form, 'create_todo': True}
        return render(request, 'newtodo.html', context)


def edit_todo(request):
    if request.POST:
        if 'edit' in request.POST:
            pk = request.POST['radiotodos']
            url = '/update_todo/' + pk
            return HttpResponseRedirect(url)
        elif 'delete' in request.POST:
            Todo.objects.get(pk=request.POST['radiotodos']).delete()
            todos = Todo.objects.order_by('created_date')
            return render(request, 'edittodo.html', {'todos': todos})
    else:
        todos = Todo.objects.order_by('created_date')
        return render(request, 'edittodo.html', {'todos': todos})

def update_todo(request, pk):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            newObject = form.save(commit=False)
            todo = Todo.objects.filter(pk=newObject.pk)
            todo.projectname = newObject.projectname
            todos = Todo.objects.order_by('created_date')
            return render(request, 'index.html', {'todos': todos})
    else:
        todo = Todo.objects.get(pk=pk)
        form = TodoForm(initial={'pk': todo.pk, 'projectname': todo.projectname, 'description': todo.description,
                                'progress': todo.progress, 'deadline': todo.deadline,
                                'created_date': todo.created_date})
        context = {'form': form, 'update_todo': True}
        return render(request, 'updatetodo.html', context)



def delete(request):
    Todo.objects.get(pk=request.DELETE['pk']).delete()


def impressum(request):
    return render(request, 'impressum.html', {})


