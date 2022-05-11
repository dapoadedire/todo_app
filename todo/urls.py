from django.urls import path
from . import views

urlpatterns = [
    path("", views.todoView, name="todoView"),
    path("addTodo/", views.addTodo, name="addTodo"),
    path("delTodo/<str:pk>/", views.delTodo, name="delTodo"),
]
