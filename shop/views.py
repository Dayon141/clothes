from django.shortcuts import render, get_object_or_404
from .models import Clothes, Brand, Size, Color
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

def registratciya(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                Login(request, user)
                return render(request, 'home.html')
        else:
            return render(request, 'login.html')
    else:
        form = Login()
    return render(request, 'login.html', {'form': form} )

def log_out(request):
    logout(request)
    return redirect('login')

def home(request):
    clothes = Clothes.objects.all()
    brands = Brand.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    
    brand_id = request.GET.get('brand')
    size_id = request.GET.get('size')
    color_id = request.GET.get('color')
    
    if brand_id:
        clothes = clothes.filter(Brand__id=brand_id)
    if size_id:
        clothes = clothes.filter(size__id=size_id)
    if color_id:
        clothes = clothes.filter(color__id=color_id)
    
    context = {
        'clothes': clothes,
        'brands': brands,
        'sizes': sizes,
        'colors': colors,
    }
    return render(request, 'home.html', context)

def clothes_detail(request, pk):
    item = get_object_or_404(Clothes, pk=pk)
    return render(request, 'clothes_detail.html', {'item': item})