from django.shortcuts import render
from todolist.models import Todo
from .forms import CreateForm
from django.shortcuts import redirect,get_object_or_404
# Create your views here.
def todo_list(request):
    data = Todo.objects.all()
    context = {"data" : data}
    return render(request,template_name='todolist/todo_list.html',context=context)

def create_task(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = CreateForm()
    return render(request,'todolist/create_task.html',{'form':form})

def edit_task(request,id):
    task = get_object_or_404(Todo,id=id)
    if request.method == "POST":
        form = CreateForm(request.POST,instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = CreateForm(instance=task)
    return render(request,'todolist/edit_task.html',{'form':form})

def mark_complete(request,id):
    task = Todo.objects.get(id=id)
    task.is_completed = "True"
    task.save()
    return redirect('/')

def delete(request,id):
    Todo.objects.get(id=id).delete()
    return redirect('/')