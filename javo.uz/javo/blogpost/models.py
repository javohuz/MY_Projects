from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    titleHome = models.CharField(max_length=200 , blank=True)
    summary = models.CharField(max_length=250 ,blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class About(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)

    skill1 = models.CharField(max_length=100 , blank=True)
    skillsize1 = models.CharField(max_length=3, blank=True)
    skill2 = models.CharField(max_length=100 , blank=True)
    skillsize2 = models.CharField(max_length=3, blank=True)
    skill3 = models.CharField(max_length=100 , blank=True)
    skillsize3 = models.CharField(max_length=3, blank=True)
    skill4 = models.CharField(max_length=100 , blank=True)
    skillsize4 = models.CharField(max_length=3, blank=True)
    skill5 = models.CharField(max_length=100 , blank=True)
    skillsize5 = models.CharField(max_length=3, blank=True)


    def __str__(self):
        return self.title



