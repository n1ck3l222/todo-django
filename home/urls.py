from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^$', views.todo_list, name='create_todo'),
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^$', views.todo_list, name='todo_list'),
]