from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
CATEGORY_CHOICES=[
    ('Repairs','Ремонт'),
    ('Education','Образование'),
    ('Beauty and health','Красота и Здоровье'),
    ('Computers','Компьютеры'),
    ('Food','Еда'),
]
class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название")
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, verbose_name="Категория")
    description = models.TextField(max_length=2048, blank=True, null=True, verbose_name="Описание")
    picture = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name="Картинка")

    class Meta:
        verbose_name="Продукт"
        verbose_name_plural="Продукты"

    def __str__(self):
        return self.name