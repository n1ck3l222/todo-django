from django.forms import ModelForm, forms
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        include = ('projectname', 'description', 'deadline')
        exclude = ('pk', 'progress', 'created_date')

class TodoUpdateForm(ModelForm):
    class Meta:
        model = Todo
        include = ('projectname', 'description', 'progress', 'deadline')
        exclude = ('pk', 'created_date')


