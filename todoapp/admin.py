from django.contrib import admin
from .models import TodoTask

# Register the TodoTask model to the admin interface
admin.site.register(TodoTask)
