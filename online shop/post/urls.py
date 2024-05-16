from django.urls import path
from post import views

from .views import ( BlogDetailView ,
                     ShopPageView ,
                     TurDetailView ,
                     BlogTurPageView ,
                     NarxDetailView ,
                     UploadView ,
                    UploadDelateView
                     )

urlpatterns = [
    path('' , BlogTurPageView.as_view(),  name='home') ,
    path('post/<int:pk>/', BlogDetailView.as_view(), name ='post') ,
    path('tur/<int:pk>/', TurDetailView.as_view(), name='tur'),
    path('narx-buyicha/<int:pk>/', NarxDetailView.as_view(), name='narx'),
    path('shop/' , ShopPageView.as_view() , name = 'shop'),
    path('buyurtmalar_timme/', UploadView.as_view(), name= 'upload'),
    path('buyurtma/', views.get , name='get' ),
    path('upload/<int:pk>/', UploadDelateView.as_view(), name='up_delate'),

]
