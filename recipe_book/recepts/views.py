from django.shortcuts import render, redirect
from .forms import AddNewRecept
from .models import Recept
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

msg: str = ''
# Create your views here.

def index(request):
    global msg
    user = ''
    #if request.COOKIES['username']:
    #    user = request.COOKIES['username']
    recepts = {}
    count = 1
    for temp in Recept.objects.all():
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'user': user})

def add(request):    
    if request.method == 'POST':
        form = AddNewRecept(request.POST, request.FILES)
        if form.is_valid():
            global msg
            user_name = request.COOKIES.get('username')

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            steps = form.cleaned_data['steps']
            time = form.cleaned_data['time']
            image = form.cleaned_data['image']
            author = User.objects.filter(name=user_name).first()
            ingredients = form.cleaned_data['ingredients']

            fs = FileSystemStorage()
            fs.save(image.name, image)

            recept = Recept(name=name, 
                            description=description, 
                            steps=steps,
                            time=time, 
                            image=image,
                            author = author, 
                            ingredients = ingredients)
            recept.save()
            msg = 'Рецепт успешно дабавлен'
    return redirect('index')