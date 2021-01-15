from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Transfer', views.Transfer, name='Transfer'),
]
