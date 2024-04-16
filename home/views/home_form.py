from django.shortcuts import render, redirect
from home.forms import HomeForm

def create(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        context = {
            'site_title': "Registrar - ",
            'form': form,
        }

        if form.is_valid():
            form.save()
            return redirect('home:cadastro')
        
        return render(request, 'home/create.html', context)
        
    context = {
        'site_title': "Registrar - ",
        'form': HomeForm(),
    }
    return render(request, 'home/create.html', context)