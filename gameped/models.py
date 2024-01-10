from django.db import models

class Video_games(models.Model):
    name=models.CharField(max_length=100),
    body=models.TextField(),
    photo=models.ImageField()
    class Meta:
        verbose_name_plural="video games"

class Product(models.Model):
    image=models.ImageField(),
    price=models.CharField(max_length=6),
    name=models.CharField(max_length=100),
    body=models.TextField()
    class Meta:
        verbose_name_plural="product"
    

class Contact(models.Model):
    name=models.CharField(max_length=100),
    email=models.EmailField(),
    phone=models.CharField(max_length=100),
    message=models.TextField()
    class Meta:
        verbose_name_plural="contact"
    




