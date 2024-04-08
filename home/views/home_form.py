from django.shortcuts import render, get_object_or_404, redirect

from home.models import Home

def create(request):
    context = {
        'site_title': "Registrar - "
    }
    return render(request, 'home/create.html', context)