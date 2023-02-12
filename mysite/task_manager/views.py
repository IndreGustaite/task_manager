from django.shortcuts import render
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.

def index(request):
    return render(request, 'index.html', context=None)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'


class TaskListCreateView(CreateView):
    model = Task
    template_name = 'taskcreate.html'
    success_url = reverse_lazy('tasks')
    form_class = TaskCreateForm


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'taskupdate.html'
    form_class = TaskUpdateForm
    context_object_name = 'taskupdate'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'taskdelete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
