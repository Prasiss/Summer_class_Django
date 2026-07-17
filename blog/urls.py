from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.blog_detail, name='blog_detail'),
    path('', views.blog, name='blog'),
]   