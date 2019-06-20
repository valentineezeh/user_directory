from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index),
    path('add/', views.add_user),
    path('list/', views.user_list),
    path('create/', views.create)
]