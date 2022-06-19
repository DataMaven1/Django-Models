from django.db import models
from django.contrib.auth.models import get_user_model

# Create your models here

User=get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)