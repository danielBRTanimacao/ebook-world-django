from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from home.forms import HomeForm, LoginHomeForm
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
            return redirect('home:user', url_id=home_id.pk)
        
        return render(request, 'home/create.html', context)
        
    context = {
        'site_title': "Registrar - ",
        'form': HomeForm(),
        'form_action': form_action,
    }
    return render(request, 'home/create.html', context)

def login(request, url_id):
    #Terminar e concerta o login
    home_user = get_object_or_404(Home, contact_id=url_id)
    form_action = reverse('home:login', args=(url_id,))

    if request.method == 'POST':
        form = LoginHomeForm(request.POST, instance=home_user)
        context = {
            'site_title': "Login - ",
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            # validadar entrada de user
            home_id = form.save()
            # fields pode coletar os nomes e validar o database
            return redirect('home:user', url_id=home_id.pk)
        
        return render(request, 'home/login.html', context)
        
    context = {
        'site_title': "Login - ",
        'form': LoginHomeForm(),
        'form_action': form_action,
    }
    return render(request, 'home/login.html', context)