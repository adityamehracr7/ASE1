from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todoView , name="todoView"),
    path('addTodo/', views.addTodo , name="addTodo"),
    path('delTodo/<todo_id>', views.delTodo, name="delTodo"),

]