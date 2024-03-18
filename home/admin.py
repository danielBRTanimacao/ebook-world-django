from django.contrib import admin

from home import models

@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = 'id', 'username', 'email',
    ordering = '-id',
    search_fields = 'id', 'username'
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = 'id', 'username'