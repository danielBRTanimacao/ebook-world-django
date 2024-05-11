from django.contrib import admin

from home import models

@admin.register(models.UsersInfos)
class UsersInfosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
    )
    ordering = '-id',
    search_fields = (
        'id',
        'username',
    )
    list_per_page = 10
    list_max_show_all = 150

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'autor_post',
    )
    ordering = '-id',
    search_fields = (
        'id',
        'autor_post',
    )
    list_per_page = 10
    list_max_show_all = 150