from django.shortcuts import render
from demo_celery.tasks import go_to_sleep


def index(request):
    task = go_to_sleep.delay(10)
    return render(request, 'app/index.html', {
        'task_id': task.task_id
    })
