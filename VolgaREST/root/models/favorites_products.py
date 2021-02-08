from django.db import models
from . import UserModel, ProductModel

class FavoritesProducts(models.Model):
   
   user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
   product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE)

   def __str__(self):
      return self.product.product
