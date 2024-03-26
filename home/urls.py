from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('<int:url_id>/index/', views.user, name='user'),
    path('search/', views.search_page, name='search'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
]