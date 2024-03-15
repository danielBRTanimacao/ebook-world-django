from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'home/cadastro.html')
    else:
        username = request.POST.get('nameInput')
        email = request.POST.get('emailInput')
        password = request.POST.get('passwordInput')
        return HttpResponse(username)