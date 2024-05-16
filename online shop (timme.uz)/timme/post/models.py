from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone


class Post(models.Model):
    turi = models.CharField(max_length=200 )
    forhome = models.CharField(max_length=200 , blank=True)
    maylike = models.CharField(max_length=200 , blank=True)
    title = models.CharField(max_length=200 )
    hometitle = models.CharField(max_length=200)
    mahsulot_soni = models.CharField(max_length=200 )
    narxi1  = models.CharField(max_length=200, blank=True)
    narxi2  = models.CharField(max_length=200, )
    narx = models.IntegerField(null=True , blank=True)
    summary = RichTextField(blank=True)
    mahsulotTavsifi = RichTextField(blank=True)
    batafsil = RichTextField(blank=True)

    photo1 = models.ImageField(upload_to='images/', blank=True)
    photo2 = models.ImageField(upload_to='images/', blank=True)
    photo3 = models.ImageField(upload_to='images/', blank=True)
    photo4 = models.ImageField(upload_to='images/', blank=True)
    photo5 = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Turlari(models.Model):
    title = models.CharField(max_length=200)
    soni = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class NarxChegara(models.Model):
    title = models.CharField(max_length=200 )
    dan = models.IntegerField(null=True , blank=True)
    gacha = models.IntegerField(null=True , blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Upload(models.Model):

    name = models.CharField(max_length=200 , blank=True)
    tel_number = models.CharField(max_length=200 , blank=True)
    number_product = models.CharField(max_length=200 , blank=True)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])