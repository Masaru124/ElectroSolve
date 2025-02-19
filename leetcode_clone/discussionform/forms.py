from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['topic','bio','first_comment']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Topic'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a short bio about the room', 'rows': 3}),
            'first_comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the first comment...', 'rows': 2}),
        }
