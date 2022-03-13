from distutils.command.upload import upload
from operator import mod
from re import T
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    desc =  models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

# in django it'll automatically add s (plural form) in database name, in category it'll be categorys and it's wrong spelling,
# if we want to customize name we can use by this
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.category_name