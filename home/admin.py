from django.contrib import admin

from home import models

@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = 'id', 'user_name',
    list_per_page = 10