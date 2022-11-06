from atexit import register
from django.contrib import admin
from .models import Task
from django.db import models
from django.forms import Textarea
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': Textarea(
                       attrs={'rows': 3,
                              'cols': 30})},
    }
    list_display = ('id','title','content','is_completed')
    list_editable = ('title','content','is_completed')
    list_per_page = 9
  
admin.site.register(Task, TaskAdmin)