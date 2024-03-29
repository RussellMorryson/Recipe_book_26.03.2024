from django.contrib import admin

# Register your models here.
from .models import Recept, Categories

admin.site.register(Recept)
admin.site.register(Categories)