from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem, Dish

main_menu = MenuItem.objects.all()
categories = Category.objects.all()
dishes = Dish.objects.all()

def index(request):
    data = {
        "main_menu": main_menu,
        "categories": categories,
    }
    return render(request, "core/index.html", context=data)

def shopping_cart_page(request):
    return render(request, "core/shopping_cart.html", {"title": 'Кошик', "main_menu": main_menu})

def contact_page(request):
    return render(request, "core/contact.html", {"title": 'Контактна інформація', "main_menu": main_menu})

def about_page(request):
    return render(request, "core/about.html", {"title": 'О сайте', "main_menu": main_menu})

def login_page(request):
    return render(request, "core/login.html", {"title": 'Вхід', "main_menu": main_menu})

def dishes_page(request, url_name):
    category = get_object_or_404(Category, url_name=url_name)
    dishes = Dish.objects.filter(category=category)

    return render(request, 'core/dishes.html', {
        'category': category,
        'dishes': dishes
        })

def salads_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
        "dishes": dishes,
    }
    return render(request, 'core/salads.html', context=data)

def drinks_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
        "dishes": dishes,
    }
    return render(request, 'core/drinks.html', context=data)

def first_courses_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
        "dishes": dishes,
    }
    return render(request, 'core/first_courses.html', context=data)

def second_courses_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
        "dishes": dishes,
    }
    return render(request, 'core/second_courses.html', context=data)

def main_courses_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
        "dishes": dishes,
    }
    return render(request, 'core/main_courses.html', context=data)

def desserts_page(request):
    data = {
        "categories": categories,
        "main_menu": main_menu,
        "dishes": dishes,
    }
    return render(request, 'core/desserts.html', context=data)