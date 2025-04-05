from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('shopping_cart/', views.shopping_cart_page, name="shopping_cart"),
    path('contact/', views.contact_page, name="contact"),
    path('about/', views.about_page, name="about"),
    path('login/', views.login_page, name="login"),
    path('<slug:url_name>/', views.dishes_page, name="dishes"),
    path('salads/', views.salads_page, name="salads"),
    path('drinks/', views.drinks_page, name="drinks"),
    path('first_courses/', views.first_courses_page, name="first_courses"),
    path('second_courses/', views.second_courses_page, name="second_courses"),
    path('main_courses/', views.main_courses_page, name="main_courses"),
    path('desserts/', views.desserts_page, name="desserts"),
]
