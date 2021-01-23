from django.db import models

# Create your models here.
class Products(models.Model):
    Item    =models.CharField(max_length=200)
    Price   =models.DecimalField(decimal_places=2, max_digits=10)
    Description=models.TextField(blank=True)
    Weight      =models.DecimalField(default=5.99, max_digits=5, decimal_places=2)