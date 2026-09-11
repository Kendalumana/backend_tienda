from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=100,decimal_places=2)
    stock = models.IntegerField()
    asset = models.BooleanField(default=True)

    def __str__(self):  
        return self.name
