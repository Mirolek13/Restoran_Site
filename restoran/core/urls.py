from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('menu/', views.menu_food_page, name="menu_food"),
    path('shopping_cart/', views.shopping_cart_page, name="shopping_cart"),
    path('contact/', views.contact_page, name="contact"),
    path('about/', views.about_page, name="about"),
    path('login/', views.login_page, name="login"),
]