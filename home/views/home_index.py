from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import UsersInfo, BookCaseUser

def index(request):
    return render(request, 'home/index.html')

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

@login_required(login_url='home:login')
def bookcase_view(request, url_id):
    user = get_object_or_404(User, pk=url_id)
    user_infos = get_object_or_404(UsersInfo, owner=url_id)
    bookcase = BookCaseUser.objects.order_by('-id')
    if request.method == 'POST':
        pass
    #test event
    context = {
        'site_title': 'Estante -',
        'home': user,
        'user_info': user_infos,
        'bookcases': bookcase,
    }
    return render(request, 'home/bookcase.html', context)