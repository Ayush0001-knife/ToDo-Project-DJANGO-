from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect

def addtask(request):
      task = request.POST['task']
      Task.objects.create(title=task)
      return redirect('home')
