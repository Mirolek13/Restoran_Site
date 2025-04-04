from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_valuable = models.BooleanField(default=True)

salads = Category.objects.create(name='Салаты')