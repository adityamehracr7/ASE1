from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import TodoItem


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def todoView(request):
    us = request.user
    print(us)
    all_items = TodoItem.objects.all()
    all_todo_items = all_items.filter(uname=us)
    print(all_todo_items)
    return render(request, 'todo/todo1.html', {'all_items': all_todo_items})


def addTodo(request):
    if request.method == "POST":
        new_item = request.POST['add']
        us = request.user
        print('working',us)
        TodoItem.objects.create(content=new_item, uname=us)
        return redirect("/todo/todo")

def delTodo(request,todo_id):
      print("working,working...........................................")
      c=TodoItem.objects.get(id=todo_id)
      c.delete()
      return redirect("/todo/todo")


def editTodo(request,todo_id):
    if request.method == "POST":
      c=TodoItem.objects.filter(id=request.POST.get('id').update(c=request.get('')))
      print("working,working...........................................")
      return redirect("/todo/todo")
