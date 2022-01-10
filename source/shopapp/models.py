from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [('other', 'Разное'), ('phones', 'Телефоны'), ('TVs', 'Телевизоры'), ('notebooks', 'Ноутбуки')]
    product_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='other', verbose_name='Категория')
    remainder = models.IntegerField(validators=[MinValueValidator(0)], null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')