from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
    path('meat', meat, name='meat'),
    path('fish', fish, name='fish'),
    path('soup', soup, name='soup'),
    path('dish', dish, name='dish'),
    path('snack', snack, name='snack'),
    path('salad', salad, name='salad'),
    path('sauce', sauce, name='sauce'),
    path('bakery', bakery, name='bakery'),
    path('desert', desert, name='desert'),
    path('cocktail', cocktail, name='cocktail'),
]