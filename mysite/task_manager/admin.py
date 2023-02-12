from django.contrib import admin
from .models import Task


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at')
    list_editable = ('user', 'title')
    list_filter = ('created_at',)


admin.site.register(Task, TaskAdmin)
