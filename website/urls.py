from django.urls import path

from .views import index, about, create, buy_product, delete

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('create/', create, name='create'),
    path('buy/<int:pk>', buy_product, name='buy'),
    path('delete/<int:pk>/', delete, name='delete'),
]