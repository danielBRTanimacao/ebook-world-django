from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search'),

    #CRUD
    path('home/<int:url_id>/detail/', views.user, name='user'),
    path('home/create/', views.create, name='cadastro'),
]