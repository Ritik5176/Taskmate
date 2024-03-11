from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def TodoList(request):
    if request.method=="POST":
        form= TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage=request.user
            form.save()
            messages.success(request,("New Task is Added!"))
        return redirect('TodoList')
    else:
        all_task= TaskList.objects.filter(manage=request.user)
        paginator=Paginator(all_task,5)
        page= request.GET.get('pg')
        all_task=paginator.get_page(page)
        return render(request, 'todolist.html', {'all_task': all_task})

def delete_task(request,task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.delete()
        return redirect('TodoList')
    else:
        messages.error(request,("You can't access the Page!"))

def edit_task(request,task_id):
    if request.method=="POST":
        task= TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            messages.success(request,("Your Task is Edited!"))
            form.save()
        return redirect('TodoList')
    else:
        task_obj= TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
    
def pending_task(request,task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=False
        task.save()
        return redirect('TodoList')
    else:
        messages.error(request,("You can't access the Page!"))

def completed_task(request,task_id):
    task= TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
        task.done=True
        task.save()
        return redirect('TodoList')
    else:
        messages.error(request,("You can't access the Page!"))
    

def Contact(request):
    context={
        "Welcome_Message": "Welcome to the TodoList App: Contact Page",
    }
    return render(request, 'contact.html', context)

def About(request):
    context={
        "Welcome_Message": "Welcome to the TodoList App: About Page",
    }
    return render(request, 'about.html', context)

def Index(request):
    context={
        "Welcome_Message": "Welcome to the TodoList App: About Page",
    }
    return render(request, 'index.html', context)
