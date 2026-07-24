from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug>/', views.page_detail, name='page_detail'),]
