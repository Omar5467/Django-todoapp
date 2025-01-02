from django.db import models

# Create your models here.
from django.db import models

class TodoTask(models.Model):
    title = models.CharField(max_length=200)  # Task title (short description)
    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['due_date']  # Order tasks by due date (oldest first)

