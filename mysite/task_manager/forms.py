from .models import Task
from django import forms


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'user']
        widgets = {'created_at': forms.HiddenInput()}


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'user']
        widgets = {'created_at': forms.HiddenInput()}
