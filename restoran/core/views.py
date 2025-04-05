from django.shortcuts import render
from .models import Category

categories = Category.objects.all()

main_menu = [
    {'title': 'Меню', 'url_name': 'menu_food'},
    {'title': 'Кошик', 'url_name': 'shopping_cart'},
    {'title': 'Контактна інформація', 'url_name': 'contact'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Вхід', 'url_name': 'login'},
]

def index(request):
    data = {
        "title": "Головна сторінка",
        "main_menu": main_menu,
    }
    return render(request, "core/index.html", context=data)

def menu_food_page(request):
    data = {
        "title": 'Меню',
        "main_menu": main_menu,
        "categories": categories,
    }
    return render(request, "core/menu.html", context=data)

def shopping_cart_page(request):
    return render(request, "core/shopping_cart.html", {"title": 'Кошик', "main_menu": main_menu})

def contact_page(request):
    return render(request, "core/contact.html", {"title": 'Контактна інформація', "main_menu": main_menu})

def about_page(request):
    return render(request, "core/about.html", {"title": 'О сайте', "main_menu": main_menu})

def login_page(request):
    return render(request, "core/login.html", {"title": 'Вхід', "main_menu": main_menu})

def salads_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
    }
    return render(request, 'core/salads.html', context=data)

def drinks_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
    }
    return render(request, 'core/drinks.html', context=data)

def first_courses_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
    }
    return render(request, 'core/first_courses.html', context=data)

def second_courses_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
    }
    return render(request, 'core/second_courses.html', context=data)

def main_courses_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
    }
    return render(request, 'core/main_courses.html', context=data)

def desserts_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
    }
    return render(request, 'core/desserts.html', context=data)