from django.shortcuts import render, redirect
from .forms import AddNewRecept
from .models import Recept
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

msg: str = ''
#username = ''
# Create your views here.

def index(request):
    global msg
    recepts = {}
    count = 1
    for temp in Recept.objects.all():
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def add(request):    
    if request.method == 'POST':
        form = AddNewRecept(request.POST, request.FILES)
        if form.is_valid():
            global msg 
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            steps = form.cleaned_data['steps']
            time = form.cleaned_data['time']
            image = form.cleaned_data['image']
            author = User.objects.filter(username=request.COOKIES.get('username')).first()
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
    form = AddNewRecept()
    return render(request, 'recepts/add.html', {'form': form, 'username': request.COOKIES.get('username')})

def meat(request):
    global msg    
    msg = "Рецепты по запросу: мясо"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='мясо'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def fish(request):
    global msg
    msg = "Рецепты по запросу: рыба"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='рыба'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def soup(request):
    global msg
    msg = "Рецепты по запросу: суп"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='суп'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})              

def dish(request):
    global msg
    msg = "Рецепты по запросу: гарнир"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='гарнир'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def snack(request):
    global msg
    msg = "Рецепты по запросу: закуска"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='закуска'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def salad(request):
    global msg
    msg = "Рецепты по запросу: салат"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='салат'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def sauce(request):
    global msg
    msg = "Рецепты по запросу: соус"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='соус'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def bakery(request):
    global msg
    msg = "Рецепты по запросу: выпечка"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='выпечка'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def desert(request):
    global msg
    msg = "Рецепты по запросу: десерт"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='десерт'):
        recepts[count] = temp
        count+=1
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})

def cocktail(request):
    global msg
    msg = "Рецепты по запросу: коктейли"   
    recepts = {}
    count = 1
    for temp in Recept.objects.filter(category='коктейли'):
        recepts[count] = temp
        count+=1    
    return render(request, 'recepts/index.html', {'recepts': recepts, 'msg': msg, 'username': request.COOKIES.get('username')})