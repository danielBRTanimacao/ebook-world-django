from django.contrib import admin

from home import models

@admin.register(models.UsersInfos)
class UsersInfosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
    )