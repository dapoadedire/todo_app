from django.shortcuts import render, redirect
# Create your views here.
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', 
        {'all_items': all_todo_items})

def addTodo(request):
    #Create a new todo item
    #save the item
    #redirect back to /todo/
    new_item= TodoItem(content= request.POST['content'])
    new_item.save()
    return redirect('/')


def delTodo(request, pk):
    item_to_delete= TodoItem.objects.get(pk=pk)
    item_to_delete.delete()
    return redirect('/')



