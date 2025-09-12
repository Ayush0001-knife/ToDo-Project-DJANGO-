from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect

def addtask(request):
      task = request.POST['task']
      Task.objects.create(title=task)
      return redirect('home')

def mark_as_done(request, pk):
      task = Task.objects.get(id=pk)
      task.is_completed = True
      task.save()
      return redirect('home')

def mark_as_undone(request,pk):
      task = Task.objects.get(id=pk)
      task.is_completed = False
      task.save()
      return redirect('home')

def deletetask(request,pk):
      task = Task.objects.get(id=pk)
      task.delete()
      return redirect('home')

def edittask(request,pk):
      task = Task.objects.get(id=pk)
      context={'task':task}
      return render(request,'edittask.html',context)

def save_edit_task(request,pk):
      task=Task.objects.get(id=pk)
      task.title=request.POST['task']
      task.save()
      return redirect('home')

