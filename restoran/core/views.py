from django.shortcuts import render


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
    return render(request, "core/menu.html", {"title": 'Меню', "main_menu": main_menu})

def shopping_cart_page(request):
    return render(request, "core/shopping_cart.html", {"title": 'Кошик', "main_menu": main_menu})

def contact_page(request):
    return render(request, "core/contact.html", {"title": 'Контактна інформація', "main_menu": main_menu})

def about_page(request):
    return render(request, "core/about.html", {"title": 'О сайте', "main_menu": main_menu})

def login_page(request):
    return render(request, "core/login.html", {"title": 'Вхід', "main_menu": main_menu})