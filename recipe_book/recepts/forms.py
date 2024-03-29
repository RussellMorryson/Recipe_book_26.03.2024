from django import forms
from .models import Categories

class AddNewRecept(forms.Form):
    name = forms.CharField(max_length=300, label='Название блюда', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(max_length=1000, label='Описание:   ', widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    steps = forms.CharField(max_length=1000, label='Действия', widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    ingredients = forms.CharField(max_length=1000, label='Ингредиенты', widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    time = forms.CharField(label='Время', widget=forms.TextInput(attrs={'class': 'form-input' }))
    image = forms.ImageField(label='Изображение')
    category = forms.ModelMultipleChoiceField(queryset=Categories.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
