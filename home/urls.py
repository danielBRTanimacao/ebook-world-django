from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('<int:url_id>/', views.user, name='user'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
]