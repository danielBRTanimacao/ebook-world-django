from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search'),

    #CRUD
    path('user/<int:url_id>/detail/', views.account, name='account'),
    path('user/<int:url_id>/<str:name_person>/', views.user, name='user'),
    path('user/<int:url_id>/<str:name_person>/update/', views.update, name='update'),
    path('user/<int:url_id>/<str:name_person>/delete/', views.delete, name='delete'),
    path('user/create/', views.create, name='cadastro'),
    path('user/login/', views.login_view, name='login'),
]