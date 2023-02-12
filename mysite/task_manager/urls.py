from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/create/', views.TaskListCreateView.as_view(), name='taskcreate'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='taskupdate'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='taskdelete'),
]