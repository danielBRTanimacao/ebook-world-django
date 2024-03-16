from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'home/index.html')

def login(request):
    if request.method == "GET":
        return render(request, 'home/login.html')
    else:
        username = request.POST.get('nameInput')
        password = request.POST.get('passwordInput')

        user = authenticate(username=username, password=password)

        if user:
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('nome ou senha invalido')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'home/cadastro.html')
    else:
        username = request.POST.get('nameInput')
        email = request.POST.get('emailInput')
        password = request.POST.get('passwordInput')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Ja existe esse safado')
        
        user = User(username=username, email=email, password=password)
        user.save()

        return HttpResponse('Usuario foi cadastrado com sucesso!')