from django.shortcuts import render
from django import forms

from home.models import Home

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = (
            'username',
            'email',
            'password',
        )

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