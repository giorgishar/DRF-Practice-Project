from re import S
from time import timezone
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
