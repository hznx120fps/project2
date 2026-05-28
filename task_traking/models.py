from django.db import models


class TrackingEntry(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} — {self.created_at:%Y-%m-%d %H:%M}"
