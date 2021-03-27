from django import forms
from .models import *
  
class postForm(forms.ModelForm):
  
    class Meta:
        model = postds
        fields = ['eventname','desc','location','image']