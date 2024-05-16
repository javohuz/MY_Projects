from django.urls import path
from .views import BlogPageView, BlogDetailView, AboutPageView, ContactPageView, BlogProjects, BlogUniversity

urlpatterns = [
    path('', BlogPageView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('projects/', BlogProjects.as_view(), name='projects'),
    path('university/', BlogUniversity.as_view(), name='university'),
]
