from django.shortcuts import render
from todos.models import Task

def home(request):
      completed_task = Task.objects.filter(is_completed=True)
      pending_task = Task.objects.filter(is_completed=False)
      context = {
            'completed_task': completed_task,
            'pending_task': pending_task
      }
      return render(request, 'home.html',context)