from django import forms
from .models import TrackingEntry


class TrackingEntryForm(forms.ModelForm):
    class Meta:
        model = TrackingEntry
        fields = ['task', 'note']
