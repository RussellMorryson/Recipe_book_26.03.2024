from django import forms
from django.contrib.auth.models import User

class AddNewRecept(forms.Form):
    name = forms.CharField(max_length=300, label='Название блюда', widget=forms.TextInput(attrs={'class': 'form-input' }))
    description = forms.CharField(max_length=1000, label='Описание:   ', widget=forms.Textarea(attrs={'cols': 61, 'rows': 5}))
    steps = forms.CharField(max_length=1000, label='Порядок действий', widget=forms.Textarea(attrs={'cols': 55, 'rows': 5}))
    #author = 
    ingredients = forms.CharField(max_length=1000, label='Ингредиенты', widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    #category = forms.CharField(max_length=50, label='Категория', widget=forms.TextInput(attrs={'class': 'form-input'}))
    time = forms.CharField(label='Время приготовления', widget=forms.TextInput(attrs={'class': 'form-input' }))
    image = forms.ImageField(label='Изображение')