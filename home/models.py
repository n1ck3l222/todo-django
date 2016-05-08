from django.db import models


# Create your models here.
from django.utils import timezone


class Todo(models.Model):
    projectname = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    progress = models.SmallIntegerField(default=0)
    deadline = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)

    "create Todo"
    def create(self):
        self.created_date=timezone.now()
        self.save()

    "edit Todo"
    def edit(self):
        self.save()







