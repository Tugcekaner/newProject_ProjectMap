from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    slug = models.SlugField(("Slug"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'  

    def __str__(self):
        return self.title
        
class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "Kullanıcı - Satıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=(
        "Kategori"), on_delete=models.CASCADE,null=True)
    title = models.CharField(("Ürün adı"), max_length=50)
    text = models.TextField(("İçerik"))
    image = models.FileField(
        ("Ürün Resmi"), upload_to='product', max_length=100)
    date_now = models.DateField(("Tarih"), auto_now_add=True)
    stok = models.IntegerField(("Stok"))
    price = models.FloatField(("Fiyat"), blank=True, null=True)

    def __str__(self):  
        return self.title
    
    class Meta:
        verbose_name_plural = 'Ürünler'
        verbose_name = 'Ürün'
