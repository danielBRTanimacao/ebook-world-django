from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect #, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.forms import RegisterForm, RegisterUpdateForm
# from home.models import UsersInfo

def create(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:index')

    context = {
        'site_title': "Registrar - ",
        'form': form,
        'register': 'Crie sua conta',
        'account_login': 'Fazer login',
        'have_account': 'ja tem uma conta?',
        'btn_send': 'Criar'
    }
    return render(request, 'home/create.html', context)

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:index')

    context = {
        'site_title': "Login - ",
        'form': form,
        'register': 'Entrar na conta',
        'account_login': 'Criar conta',
        'have_account': 'não tem uma conta?',
        'btn_send': 'Entrar'
    }

    return render(request, 'home/login.html', context)

@login_required(login_url='home:login')
def update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        context = {
            'site_title': "Update - ",
            'form': form,
            'register': 'Update na conta',
            'btn_send': 'Enviar'
        }
        return render(request, 'home/create.html', context)
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'contact/create.html', context)
    
    form.save()
    return redirect('contact:update')

@login_required(login_url='home:login')
def logout_view(request):
    auth.logout(request)
    return redirect('home:login')