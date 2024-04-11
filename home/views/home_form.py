from django.shortcuts import render
from home.forms import HomeForm

def create(request):
    if request.method == 'POST':
        context = {
            'site_title': "Registrar - ",
            'form': HomeForm(request.POST),
        }
        return render(request, 'home/create.html', context)
        
    context = {
        'site_title': "Registrar - ",
        'form': HomeForm(),
    }
    return render(request, 'home/create.html', context)