from django import forms
from .models import Apply  # Assuming you have a JobApplication model in models.py

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website','cv', 'coverletter']

