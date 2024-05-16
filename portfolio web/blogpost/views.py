from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView)
from .models import Post, About
from hitcount.views import HitCountDetailView


# Create your views here.
def error404(request, exception):
    return render(request, '404.html')


class BlogPageView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BlogProjects(ListView):
    model = Post
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BlogUniversity(ListView):
    model = Post
    template_name = 'university.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BlogDetailView(HitCountDetailView):
    model = Post
    template_name = 'post.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class AboutPageView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'About'


class ContactPageView(TemplateView):
    model = Post
    template_name = 'contact.html'





