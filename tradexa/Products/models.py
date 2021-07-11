from django.db import models
from datetime import date
# Create your models here.



class Product(models.Model):
    name=models.CharField(max_length=30, default="")
    weight=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    created_at=models.DateField(default=date.today)
    updated_at=models.DateField(default=date.today)

    def __str__(self):
        return self.name