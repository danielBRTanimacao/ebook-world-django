from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.forms import RegisterForm, RegisterUpdateForm
from home.models import UsersInfos

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
def update(request, url_id, name_person):
    update_user = get_object_or_404(User, pk=url_id, username=name_person)
    user_infos = get_object_or_404(UsersInfos, owner=request.user)
    form_action = reverse('home:update', args=(url_id,))

    if request.method == "POST":
        form = RegisterUpdateForm(request.POST, request.FILES, instance=update_user)
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Update - '
        }

        if form.is_valid():
            user = form.save()
            return redirect('home:update', url_id=user.pk)
        
        return render(request, 'home/create.html', context)
    context = {
        'form': RegisterUpdateForm(instance=update_user),
        'form_action': form_action,
        'site_title': 'Update - ',
    }
    return render(request, 'home/create.html', context)

@login_required(login_url='home:login')
def delete(request):
    return render(request, 'home:index')

@login_required(login_url='home:login')
def logout_view(request):
    auth.logout(request)
    return redirect('home:login')