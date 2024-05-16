from django.shortcuts import render
from django.views.generic import (ListView, TemplateView , DeleteView )
from .models import Post, Turlari , NarxChegara , Upload
from hitcount.views import HitCountDetailView
from .forms import UploadForms
from django.urls import reverse_lazy
from django.http import HttpResponse


def get(request):
    if request.POST:
        form = UploadForms(request.POST , request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return render(request , 'get01.html')
    return render(request , 'get.html' , {'form' : UploadForms})

class UploadDelateView(DeleteView):
    model = Upload
    template_name = 'up_delate.html'
    success_url = reverse_lazy('upload')




def error404(request , exception ):
    return render(request , '404.html')
class BlogPageView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # or whatever
        context['turlar'] = Turlari.objects.all()  # or whatever
        context['narx'] = NarxChegara.objects.all()  # or whatever

        return context

class BlogDetailView(HitCountDetailView):
    model = Post
    template_name = 'post.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['turlar'] = Turlari.objects.all()
        return context


class TurDetailView(HitCountDetailView):
    model = Turlari
    template_name = 'tur.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # or whatever
        context['turlar'] = Turlari.objects.all()  # or whatever
        context['narx'] = NarxChegara.objects.all()  # or whatever
        return context


class NarxDetailView(HitCountDetailView):
    model = NarxChegara
    template_name = 'narxchegara.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # or whatever
        context['turlar'] = Turlari.objects.all()  # or whatever
        context['narx'] = NarxChegara.objects.all()  # or whatever
        return context

class BlogTurPageView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # or whatever
        context['turlar'] = Turlari.objects.all()  # or whatever
        return context

class ShopPageView(TemplateView):
    model = Post
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # or whatever
        context['turlar'] = Turlari.objects.all()  # or whatever
        context['narx'] = NarxChegara.objects.all()  # or whatever
        return context

class UploadView(ListView):
    model = Upload
    template_name = 'upload.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upload'] = Upload.objects.all()  # or whatever
        context['turlar'] = Turlari.objects.all()  # or whatever
        context['posts'] = Post.objects.all()  # or whatever
        return context





