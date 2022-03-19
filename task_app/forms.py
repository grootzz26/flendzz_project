from django import forms
from .models import studentDB

class studentForm(forms.ModelForm):

    class Meta:
        model = studentDB
        fields = ['rollnumber','name','DOB','marks']