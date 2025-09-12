from django.urls import path
from . import views

urlpatterns=[
      path('addtask/',views.addtask,name='addtask'),
      path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
      path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
      path('deletetask/<int:pk>/',views.deletetask,name='deletetask'),
      path('edittask/<int:pk>/',views.edittask,name='edittask'),
      path('save_edit_task/<int:pk>/',views.save_edit_task,name='save_edit_task'),
]
