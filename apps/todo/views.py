from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    tasks = Todo.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


@login_required(login_url='login')
def create_task(request):
    form = TodoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'todo/add.html', context)


@login_required(login_url='login')
def delete_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')


@login_required(login_url='login')
def update_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'todo': todo, 'form': form}
    return render(request, 'todo/update.html', context)


@login_required(login_url='login')
def complete_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')
