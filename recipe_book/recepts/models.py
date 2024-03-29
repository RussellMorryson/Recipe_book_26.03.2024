from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recept(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    steps = models.CharField(max_length=4000)    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=1000)
    time = models.CharField(max_length=10)    
    image = models.ImageField(upload_to='')
    category = models.CharField(max_length=50)

    def __str__(self):
        return f'Name: {self.name}, author: {self.author}'
    
class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f'Name: {self.category}'