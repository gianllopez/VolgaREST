from django.db import models
from . import UserModel

class ProductModel(models.Model):

   user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
   images = models.TextField(max_length=2048)
   product = models.CharField(max_length=50)
   price = models.CharField(max_length=15)
   description = models.TextField(max_length=145, null=True, blank=True)
   tags = models.TextField(max_length=500, null=True, blank=True)
   key = models.CharField(max_length=10, primary_key=True)

   def __str__(self):
      return f'{self.product} from {self.user.username}'
