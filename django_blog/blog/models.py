from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): # post is the table name
    title=models.CharField(max_length=100)
    content=models.TextField() #unrestricted text
    date_posted=models.DateField(default=timezone.now) 
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title