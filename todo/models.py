from datetime import datetime
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50, null = False)
    content = models.TextField(max_length = 200, null = False, default="content")
    is_completed = models.BooleanField(default = False)