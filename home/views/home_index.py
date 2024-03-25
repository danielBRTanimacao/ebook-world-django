from django.shortcuts import render, get_object_or_404

from home.models import Home

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def cadastro(request):
    return render(request, 'home/cadastro.html')

def user(request, url_id):
    user_single = get_object_or_404(Home, pk=url_id)

    context = {
        'home': user_single,
    }

    return render(request, 'home/user.html', context)

def search_page(request):
    search_query = request.GET.get('q')
    context = {
        'query': search_query,
    }
    return render(request, 'home/search.html', context)

def specific_book(request, id_book):
    class Book:
        def __init__(self) -> None:
            self.id = id_book
            self.name = "nome"
            self.img_book = "img"
            self.description = "description"
        
    context = {
        "book_id": Book,
    }
    return render(request, 'home/specific_book.html', context)