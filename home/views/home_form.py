from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse
from home.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def create(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:account')

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
    form = LoginForm(request)

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

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
def update(request, url_id, name_person):
    home_user = get_object_or_404(User, pk=url_id, username=name_person)
    form_action = reverse('home:update', args=(url_id, name_person,))

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=home_user)

        context = {
            'site_title': "Update - ",
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            home_id = form.save()
            return redirect('home:account', url_id=home_id.pk)
        
        return render(request, 'home/create.html', context)
        
    context = {
        'site_title': "Update - ",
        'form': RegisterForm(instance=home_user),
        'form_action': form_action,
    }
    return render(request, 'home/create.html', context)

@login_required(login_url='home:login')
def delete(request, url_id, name_person):
    home_user = get_object_or_404(User, pk=url_id, username=name_person)

    confirmation = request.POST.get('confirmation', 'no')
 
    if confirmation == 'yes':
        home_user.delete()
        return redirect('home:index')

    context =  {
        'site_title': "Delete - ",
        'home': home_user,
        'confirmation': confirmation,
    }

    return render(request, 'home/user.html', context)

@login_required(login_url='home:login')
def logout_view(request):
    auth.logout(request)
    return redirect('home:login')