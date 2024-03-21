from django.shortcuts import render, get_object_or_404

from home.models import Home

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def cadastro(request):
    return render(request, 'home/cadastro.html')

def user(request, url_id):
    user_single = get_object_or_404(Home, pk=url_id)

    context = {
        'home': user_single,
    }

    return render(request, 'home/user.html', context)