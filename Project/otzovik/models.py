from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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

    def get_rate(self):
        reviews = self.review.all().exclude(is_moder=False)
        rate = 0
        if reviews.count()>0:
            for review in reviews:
                rate+=review.rate
            rate=rate/reviews.count()
        return rate


class Review(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='review' ,verbose_name='Автор' )
    product = models.ForeignKey('otzovik.Product', on_delete=models.CASCADE, related_name='review', verbose_name='Продукт')
    text = models.TextField(max_length=4096, verbose_name='Текст отзыва')
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    is_moder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

    def __str__(self):
        return f'{self.author.username} - {self.product.name}'