from django.shortcuts import render
from .models import TrackingEntry


def tracking_list(request):
    entries = TrackingEntry.objects.select_related('task').all()
    return render(request, 'task_traking/index.html', {'entries': entries})
