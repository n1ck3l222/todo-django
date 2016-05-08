from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^create_todo/$', views.create_todo, name='create_todo'),
    url(r'^edit_todo/$', views.edit_todo, name='edit_todo'),
    url(r'^edit_todo/(?P<pk>\d+)/$', views.update_todo, name='update_todo'),
    url(r'^impressum/$', views.impressum, name='impressum'),
]