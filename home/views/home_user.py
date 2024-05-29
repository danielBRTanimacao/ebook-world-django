from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from home.forms import FormForPost
from django.contrib.auth.models import User
from home.models import UsersInfo, Post

def user_view(request, url_id, name_person):
    '''
        user_view: request, url_id: int, name_person: str
        url_id => recebe um valor inteiro referente a um usuario existente
        name_person => recebe uma string referente ao nome de um usuario existente

        return ---> render template 'user'
    '''
    user_single = get_object_or_404(User, pk=url_id, username=name_person)
    user_infos = get_object_or_404(UsersInfo, owner=url_id)
    context = {
        'home': user_single,
        'user_info': user_infos,
        'site_title': f"{user_single.username} - ",
    }
    return render(request, 'home/user.html', context)

@login_required(login_url='home:login')
def account(request, url_id):
    '''
        account: request, url_id: int
            ---> principal conta do usuario token segurança
        url_id => recebe um valor inteiro referente a um usuario existente
        Decorator @login_required() função retorna se o usuario esta logado ou não

        return ---> render template 'user' com token
    '''
    user_single = get_object_or_404(User, pk=url_id)
    #objects usuario
    try:
        user_infos = get_object_or_404(UsersInfo, owner=url_id)
        # objects informações do usuario
    except: #tratar esse erro aqui
        infos = UsersInfo()
        infos.owner = request.user
        infos.save()
        user_infos = get_object_or_404(UsersInfo, owner=url_id)

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
    user_infos = get_object_or_404(UsersInfo, owner=url_id)
    context = {
        'home': user_single,
        'user_info': user_infos,
        'site_title': f"{user_single.username} Config - ",
    }
    return render(request, 'home/config.html', context)