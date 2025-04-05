from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50, default='default_name')
    url_name = models.CharField(max_length=100, default="default-slug")

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, default='default_name')
    url_name = models.SlugField(max_length=100, default="default-slug")

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_valuable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
