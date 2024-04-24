from django.shortcuts import render, get_object_or_404, redirect

from home.models import Home

def index(request):
    return render(request, 'home/index.html')

def user(request, url_id, name_person):
    user_single = get_object_or_404(Home, pk=url_id)
    if name_person != user_single.username:
        return redirect('home:index')
    context = {
        'home': user_single,
        'site_title': f"{user_single.username} - ",
    }
    return render(request, 'home/user.html', context)

# Criar permissão para este usuario
def account(request, url_id):
    user_single = get_object_or_404(Home, pk=url_id)
    context = {
        'home': user_single,
        'site_title': f"{user_single.username} - ",
    }
    return render(request, 'home/account.html', context)

def search_page(request):
    search_query = request.GET.get('q', '').strip()
    if search_page == '':
        return redirect('home:index')
    context = {
        'query': search_query,
        'site_title': f"{search_query} - ",
    }
    return render(request, 'home/search.html', context)

def specific_book(request, id_book):
    context = {
        "book_id": id_book,
        'site_title': "name - "
    }
    return render(request, 'home/specific_book.html', context)