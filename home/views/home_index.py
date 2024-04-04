import os
from django.shortcuts import render, get_object_or_404, redirect

from home.models import Home

def index(request):
    return render(request, 'home/index.html')

def login(request):
    context = {
        'site_title': "Login - "
    }
    return render(request, 'home/login.html', context)

def cadastro(request):
    context = {
        'site_title': "Registrar - "
    }
    return render(request, 'home/create.html', context)

def user(request, url_id):
    user_single = get_object_or_404(Home, pk=url_id)
    context = {
        'home': user_single,
        'site_title': f"{user_single.username} - ",
    }
    return render(request, 'home/user.html', context)

def search_page(request):
    API_KEY_BOOK = os.getenv('API_BOOK_KEY')
    search_query = request.GET.get('q', '').strip()
    if search_page == '':
        return redirect('home:index')
    context = {
        'query': search_query,
        'site_title': f"{search_query} - ",
        'api_key': API_KEY_BOOK,
    }
    return render(request, 'home/search.html', context)

def specific_book(request, id_book):
    context = {
        "book_id": id_book,
        'site_title': "name - "
    }
    return render(request, 'home/specific_book.html', context)