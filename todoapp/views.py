from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoTask


# View to list tasks and handle add/update
def task_list(request):
    if request.method == 'POST':
        if 'add_task' in request.POST:  # Check if it's adding a new task
            title = request.POST.get('title')
            if title:
                TodoTask.objects.create(title=title)
        elif 'update_task' in request.POST:  # Handle updating task
            task_id = request.POST.get('task_id')
            title = request.POST.get('title')
            task = get_object_or_404(TodoTask, id=task_id)
            task.title = title
            task.save()
        elif 'delete_task' in request.POST:  # Handle deleting task
            task_id = request.POST.get('task_id')
            task = get_object_or_404(TodoTask, id=task_id)
            task.delete()

        return redirect('task_list')  # Redirect to the same page after action

    tasks = TodoTask.objects.all()  # Fetch all tasks
    return render(request, 'task_list.html', {'tasks': tasks})

