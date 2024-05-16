from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from home.forms import FormForPost
from django.contrib.auth.models import User
from home.models import UsersInfos, Post

def index(request):
    return render(request, 'home/index.html')

def user_view(request, url_id, name_person):
    user_single = get_object_or_404(User, pk=url_id, username=name_person)
    user_infos = get_object_or_404(UsersInfos, owner=url_id)
    context = {
        'home': user_single,
        'user_info': user_infos,
        'site_title': f"{user_single.username} - ",
    }
    return render(request, 'home/user.html', context)

@login_required(login_url='home:login')
def account(request, url_id):
    user_single = get_object_or_404(User, pk=url_id)
    try:
        user_infos = get_object_or_404(UsersInfos, owner=url_id)
    except: #tratar esse erro aqui
        infos = UsersInfos()
        infos.owner = request.user
        infos.save()
        user_infos = get_object_or_404(UsersInfos, owner=url_id)

    posts = Post.objects.order_by('-id')

    if request.method == "POST":
        form = FormForPost(request.POST, request.FILES)
        context = {
            'home': user_single,
            'user_info': user_infos,
            'post': posts,
            'form_post': form,
            'site_title': f"{user_single.username} - ",
        }

        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.autor_post = request.user
            post_form.save()
            return redirect('home:account', url_id=url_id)

        return render(request, 'home/user.html', context)

    context = {
        'home': user_single,
        'user_info': user_infos,
        'post': posts,
        'form_post': FormForPost(),
        'site_title': f"{user_single.username} - ",
    }
    return render(request, 'home/user.html', context)

@login_required(login_url='home:login')
def config_account(request, url_id):
    user_single = get_object_or_404(User, pk=url_id)
    user_infos = get_object_or_404(UsersInfos, owner=url_id)
    context = {
        'home': user_single,
        'user_info': user_infos,
        'site_title': f"{user_single.username} Config - ",
    }
    return render(request, 'home/config.html', context)

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

def bookcase_view(request):
    context = {
        'site_title': 'Estante -',
    }
    return render(request, 'home/bookcase.html', context)