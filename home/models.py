from django.db import models
from django.contrib.auth.models import User

# class BookCaseUser(models.Model):
#     img_book
#     name
#     autor
#     number_pages

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
    post_picture = models.ImageField(blank=True, upload_to='posts/%Y/%m/')
    autor_post = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.simple_text[0:100]
    
# class PostComments(models.Model):
