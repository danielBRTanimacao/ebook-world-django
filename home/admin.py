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

@admin.register(models.PostComments)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner_comment', 'owner_user_comment',)
    ordering = '-id',
    search_fields = (
        'id',
        'owner_comment',
    )
    list_per_page = 10
    list_max_show_all = 150

@admin.register(models.BookCaseUser)
class BookCaseUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner_book',)
    ordering = '-id',
    search_fields = (
        'id',
        'owner_book',
    )
    list_per_page = 10
    list_max_show_all = 150