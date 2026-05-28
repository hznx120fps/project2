from django.http import HttpResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    lines = [f"{task.title} — {'готово' if task.completed else 'в процессе'}" for task in tasks]
    return HttpResponse('<br>'.join(lines) or 'Нет задач')
