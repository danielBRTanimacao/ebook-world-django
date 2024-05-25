from django.db import models
from django.contrib.auth.models import User

class BookCaseUser(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    img = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200, blank=True)
    number_pages = models.PositiveBigIntegerField(default=0)
    # tag

class UsersInfos(models.Model):
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    total_pages_read = models.PositiveBigIntegerField(default=0)
    total_books = models.PositiveBigIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class Post(models.Model):
    simple_text = models.CharField(max_length=200, blank=True)
    likes = models.PositiveBigIntegerField(default=0)
    date_posted = models.DateField(auto_now=True)
    picture = models.ImageField(blank=True, upload_to='posts/%Y/%m/')
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.simple_text[0:100]
    
class PostComments(models.Model):
    owner_user_comment = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    owner_comment = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.TextField(blank=True)
    likes = models.PositiveBigIntegerField(default=0)
    fixed = models.BooleanField(default=False)

