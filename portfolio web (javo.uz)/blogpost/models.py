# from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    where_home = models.CharField(max_length=2, blank=True)
    where_projects = models.CharField(max_length=2, blank=True)
    where_university = models.CharField(max_length=2, blank=True)
    where_carusel = models.CharField(max_length=2, blank=True)
    title = models.CharField(max_length=200)
    titleHome = models.CharField(max_length=200, blank=True)
    summary = models.CharField(max_length=250, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    photo_carusel = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class About(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
