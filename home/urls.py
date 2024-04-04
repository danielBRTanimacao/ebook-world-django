from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search'),

    #CRUD
    path('home/cadastro/', views.cadastro, name='cadastro'),
    path('home/login/', views.login, name='login'),
    path('home/<int:url_id>/detail/', views.user, name='user'),
]