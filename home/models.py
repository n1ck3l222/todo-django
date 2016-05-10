from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
from django.utils import timezone


class Todo(models.Model):
    projectname = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    progress = models.SmallIntegerField(default=0)
    deadline = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolut_url(self):
        return reverse('todo-detail', kwargs={'pk': self.pk})