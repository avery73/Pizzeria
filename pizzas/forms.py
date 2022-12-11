from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['description','image']
        labels = {'description': 'What would you like to say?'}