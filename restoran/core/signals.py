from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name == 'core':
        Category.objects.get_or_create(name='Салати', url_name="salads")
        Category.objects.get_or_create(name='Напої', url_name="drinks")
        Category.objects.get_or_create(name="Перші страви", url_name="first_courses")
        Category.objects.get_or_create(name="Другі страви", url_name="second_courses")
        Category.objects.get_or_create(name="Основні страви", url_name="main_courses")
        Category.objects.get_or_create(name="Десерти", url_name="desserts")
        
        