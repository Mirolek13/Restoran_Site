from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import Category, MenuItem, Dish

# @receiver(post_migrate)
# def create_default_categories(sender, **kwargs):
#     if sender.name == 'core':
#         Category.objects.get_or_create(name='Салати', url_name="salads")
#         Category.objects.get_or_create(name='Напої', url_name="drinks")
#         Category.objects.get_or_create(name="Перші страви", url_name="first_courses")
#         Category.objects.get_or_create(name="Другі страви", url_name="second_courses")
#         Category.objects.get_or_create(name="Основні страви", url_name="main_courses")
#         Category.objects.get_or_create(name="Десерти", url_name="desserts")
        
# @receiver(post_migrate)
# def create_default_main_menu(sender, **kwargs):
#     if sender.name == 'core':
#         MenuItem.objects.get_or_create(name='Головна Сторінка', url_name="home")
#         MenuItem.objects.get_or_create(name='Кошик', url_name="shopping_cart")
#         MenuItem.objects.get_or_create(name='Контактна інформація', url_name="contact")
#         MenuItem.objects.get_or_create(name="О сайте", url_name="about")
#         MenuItem.objects.get_or_create(name="Вхід", url_name="login")

# @receiver(post_save, sender=Category)
# def create_default_dishes(sender, instance, created, **kwargs):
#     if created and instance.name == "Салати":
#         Dish.objects.get_or_create(name="Олів'є по-домашньому", category=instance, price=89)
#         Dish.objects.get_or_create(name="Грецький салат з бринзою", category=instance, price=115)
#         Dish.objects.get_or_create(name="Салат з куркою та ананасом", category=instance, price=100)
#     elif created and instance.name == "Напої":
#         Dish.objects.get_or_create(name="Fanta (1,25 л)", category=instance, price=40)
#         Dish.objects.get_or_create(name="Сoca cola (750 мл)", category=instance, price=29)
#         Dish.objects.get_or_create(name="Pepsi (1 л)", category=instance, price=35)
#     elif created and instance.name == "Перші страви":
#         Dish.objects.get_or_create(name="Борщ український зі сметаною", category=instance, price=90)
#         Dish.objects.get_or_create(name="Курячий бульйон з локшиною", category=instance, price=75)
#         Dish.objects.get_or_create(name="Грибна юшка з перловкою", category=instance, price=87)
#     elif created and instance.name == "Другі страви":
#         Dish.objects.get_or_create(name="Картопля по-селянськи з грибами", category=instance, price=103)
#         Dish.objects.get_or_create(name="Тушкована капуста з ковбасками", category=instance, price=105)
#         Dish.objects.get_or_create(name="Каша гречана з печінкою", category=instance, price=100)
#     elif created and instance.name == "Основні страви":
#         Dish.objects.get_or_create(name="Котлета по-київськи з картопляним пюре", category=instance, price=130)
#         Dish.objects.get_or_create(name="Стейк зі свинини з овочами гриль", category=instance, price=179)
#         Dish.objects.get_or_create(name="Філе куряче в вершковому соусі з рисом", category=instance, price=145)
#     elif created and instance.name == "Десерти":
#         Dish.objects.get_or_create(name="Сирники зі сметаною та варенням", category=instance, price=79)
#         Dish.objects.get_or_create(name="Штрудель яблучний з морозивом", category=instance, price=95)
#         Dish.objects.get_or_create(name="Медівник домашній", category=instance, price=70)

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'core':
        salads, _ = Category.objects.get_or_create(name='Салати', url_name="salads")
        drinks, _ = Category.objects.get_or_create(name='Напої', url_name="drinks")
        first_courses, _ = Category.objects.get_or_create(name="Перші страви", url_name="first_courses")
        second_courses, _ = Category.objects.get_or_create(name="Другі страви", url_name="second_courses")
        main_courses, _ = Category.objects.get_or_create(name="Основні страви", url_name="main_courses")
        desserts, _ = Category.objects.get_or_create(name="Десерти", url_name="desserts")

        MenuItem.objects.get_or_create(name='Головна Сторінка', url_name="home")
        MenuItem.objects.get_or_create(name='Кошик', url_name="shopping_cart")
        MenuItem.objects.get_or_create(name='Контактна інформація', url_name="contact")
        MenuItem.objects.get_or_create(name="О сайте", url_name="about")
        MenuItem.objects.get_or_create(name="Вхід", url_name="login")

        Dish.objects.get_or_create(name="Олів'є по-домашньому", category=salads, price=89, img="images/SaladOlivie.jpeg")
        Dish.objects.get_or_create(name="Грецький салат з бринзою", category=salads, price=115, img="images/SaladGreece.jpeg")
        Dish.objects.get_or_create(name="Салат з куркою та ананасом", category=salads, price=100, img="images/SaladPineapple.jpeg")

        Dish.objects.get_or_create(name="Fanta (0,33л)", category=drinks, price=28, img="images/Fanta.jpg")
        Dish.objects.get_or_create(name="Сoca cola (0,33л)", category=drinks, price=29, img="images/CocaCola.jpeg")
        Dish.objects.get_or_create(name="Pepsi (0,33л)", category=drinks, price=27, img="images/Pepsi.jpeg")

        Dish.objects.get_or_create(name="Борщ український зі сметаною", category=first_courses, price=90, img="images/Borsh.jpeg")
        Dish.objects.get_or_create(name="Курячий бульйон з локшиною", category=first_courses, price=75, img="images/ChickenSoup.png")
        Dish.objects.get_or_create(name="Грибна юшка з перловкою", category=first_courses, price=87, img="images/MushroomSoup.jpg")

        Dish.objects.get_or_create(name="Картопля по-селянськи з грибами", category=second_courses, price=103, img="images/PotatoMushroom.png")
        Dish.objects.get_or_create(name="Тушкована капуста з ковбасками", category=second_courses, price=105, img="images/CabbageSausages.jpeg")
        Dish.objects.get_or_create(name="Каша гречана з печінкою", category=second_courses, price=100, img="images/PorridgeLiver.jpg")

        Dish.objects.get_or_create(name="Котлета по-київськи з картопляним пюре", category=main_courses, price=130, img="images/Kotleta.jpg")
        Dish.objects.get_or_create(name="Стейк зі свинини з овочами гриль", category=main_courses, price=179, img="images/Steak.jpg")
        Dish.objects.get_or_create(name="Філе куряче в вершковому соусі з рисом", category=main_courses, price=145, img="images/ChickenFillet.jpg")

        Dish.objects.get_or_create(name="Сирники зі сметаною та варенням", category=desserts, price=79, img="images/Cheesecakes.jpg")
        Dish.objects.get_or_create(name="Штрудель яблучний з морозивом", category=desserts, price=95, img="images/AppleStrudel.jpg")
        Dish.objects.get_or_create(name="Медівник домашній", category=desserts, price=70, img="images/Medovik.png")
