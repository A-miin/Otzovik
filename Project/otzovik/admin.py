from django.contrib import admin
from .models import Product, Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'author', 'rate']
    fields = ['id', 'product', 'author', 'text', 'rate','is_moder', 'created_at', 'updated_at' ]
    readonly_fields = ['id', 'created_at', 'updated_at']

admin.site.register(Product)
admin.site.register(Review, ReviewAdmin)