from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import RegisterForm

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
    return render(request, 'home:index')

@login_required(login_url='home:login')
def delete(request):
    return render(request, 'home:index')

@login_required(login_url='home:login')
def logout_view(request):
    auth.logout(request)
    return redirect('home:login')