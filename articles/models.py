from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from PIL import Image
import os
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
        SIZE = 1050, 700

        if self.photo:
            pic = Image.open(self.photo.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.photo.path)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
    