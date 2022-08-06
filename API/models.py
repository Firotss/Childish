from django.db import models

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length = 30)
    Price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    Date = models.DateField()
    Products = models.ManyToManyField(Product)