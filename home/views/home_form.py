from django.shortcuts import render, redirect
from django.urls import reverse
from home.forms import HomeForm, LoginHomeForm

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

def login(request):
    #Terminar e concerta o login
    form_action = reverse('home:login')

    if request.method == 'POST':
        form = LoginHomeForm(request.POST)
        context = {
            'site_title': "Login - ",
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            home_id = form
            return redirect('home:user', url_id=home_id.pk)
        
        return render(request, 'home/login.html', context)
        
    context = {
        'site_title': "Login - ",
        'form': LoginHomeForm(),
        'form_action': form_action,
    }
    return render(request, 'home/login.html', context)