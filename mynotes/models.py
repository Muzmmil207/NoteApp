from django.db import models
from datetime import datetime, date
# Create your models here.

class CreateNote(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.created_date}" 
