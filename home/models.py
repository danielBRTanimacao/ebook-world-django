from django.db import models
from django.utils import timezone

class Home(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    # picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    all_books = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    all_pages = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self) -> str:
        return self.username
    