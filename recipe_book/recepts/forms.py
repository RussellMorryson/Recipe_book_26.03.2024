from django import forms
from django.contrib.auth.models import User

class AddNewRecept(forms.Form):
    name = forms.CharField(max_length=300, label='Название', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=1000, label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    steps = forms.CharField(max_length=1000, label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    time = forms.TimeField(widget=forms.TimeInput)
    image = forms.ImageField(widget=forms.ImageField)
    #author = 
    ingredients = forms.CharField(max_length=1000, label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
