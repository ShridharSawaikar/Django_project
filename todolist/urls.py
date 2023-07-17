from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list,name="todo_list"),
    path('create/new/',views.create_task,name="create_task"),
    path('edit/<int:id>/',views.edit_task,name="edit_task"),
    path('complete/<int:id>/',views.mark_complete,name="mark_complete"),
    path('delete/<int:id>/',views.delete,name="delete"),
]