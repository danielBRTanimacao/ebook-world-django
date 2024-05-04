from django.db import models
from django.contrib.auth.models import User

class UsersInfos(models.Model):
    username = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    