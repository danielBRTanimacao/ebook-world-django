from django.contrib import admin

from home import models

@admin.register(models.HomeCadastroUser)
class HomeCadastroUserAdmin(admin.ModelAdmin):
    list_display = 'id', 'username', 'email'
    list_per_page = 10