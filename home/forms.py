from django.forms import ModelForm, forms
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        include = ('projectname', 'description', 'progress', 'deadline')
        exclude = ('progress', 'created_date')


