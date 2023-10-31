from django import forms
from .models import Apply, Job  # Assuming you have a JobApplication model in models.py


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'coverletter']


class PostJop(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner', 'slug')
