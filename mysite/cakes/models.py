from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product = models.CharField(max_length=30)
    images = models.ImageField(upload_to='images')
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return self.product


class Sample(models.Model):
    sample = models.CharField(max_length=30)
    images = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.sample


class Filling(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.TextField(max_length=30)
    date = models.DateField()
    weight = models.IntegerField(default=2, validators=[MaxValueValidator(30), MinValueValidator(1)])
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    filling = models.ForeignKey(Filling, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.name

