from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView)
from .models import Post, About
from hitcount.views import HitCountDetailView

# Create your views here.
def error404(request , exception ):
    return render(request , '404.html')
class BlogPageView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(HitCountDetailView):
    model = Post
    template_name = 'post.html'
    count_hit = True

class AboutPageView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'About'


class ContactPageView(TemplateView):
    model = Post
    template_name = 'contact.html'





