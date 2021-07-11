from django.db import models
from django.contrib.auth.models import User
from datetime import date



# Create your models here.

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    text = models.TextField(default="")
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(default=date.today)

    def __str__(self):
        return( self.text[:10]+ "... by - "+ self.user.username)
