from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
# Create your models here.

class Site(models.Model):
    title = models.CharField(max_length = 50)
    template = models.CharField(max_length = 100)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

class Function(models.Model):
    name = models.CharField(max_length = 50)

class SiteFunction(models.Model):
    site = models.ForeignKey(Site, on_delete = models.CASCADE)
    function = models.ForeignKey(Function, on_delete = models.CASCADE)


#-------------------- Online Store start-----------------------
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=8)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)



    def __str__(self):
        return self.title


#-------------------- Online Store end-----------------------