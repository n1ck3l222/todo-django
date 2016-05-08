from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        include = ('projectname', 'description', 'deadline')
        exclude = ('progress', 'created_date')


