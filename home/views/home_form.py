from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.urls import reverse
from home.forms import HomeForm
from home.models import Home

def create(request):
    form_action = reverse('home:cadastro')

    if request.method == 'POST':
        form = HomeForm(request.POST)
        context = {
            'site_title': "Registrar - ",
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            home_id = form.save()
            return redirect('home:account', url_id=home_id.pk)
        
        return render(request, 'home/create.html', context)
        
    context = {
        'site_title': "Registrar - ",
        'form': HomeForm(),
        'form_action': form_action,
        'register': 'Crie sua conta'
    }
    return render(request, 'home/create.html', context)

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:account')

    context = {
        'site_title': "Login - ",
        'form': form,
        'register': 'Login',
    }
    return render(request, 'home/login.html', context)

def update(request, url_id, name_person):
    home_user = get_object_or_404(Home, pk=url_id, username=name_person)
    form_action = reverse('home:update', args=(url_id, name_person,))

    if request.method == 'POST':
        form = HomeForm(request.POST, instance=home_user)

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
        'form': HomeForm(instance=home_user),
        'form_action': form_action,
    }
    return render(request, 'home/create.html', context)


def delete(request, url_id, name_person):
    home_user = get_object_or_404(Home, pk=url_id, username=name_person)

    confirmation = request.POST.get('confirmation', 'no')
 
    if confirmation == 'yes':
        home_user.delete()
        return redirect('home:index')

    context =  {
        'site_title': "Delete - ",
        'home': home_user,
        'confirmation': confirmation,
    }

    return render(request, 'home/account.html', context)