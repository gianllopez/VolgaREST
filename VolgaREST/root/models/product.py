from django.db import models
from . import UserModel

class ProductModel(models.Model):

   user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

   image_1 = models.CharField()
   image_2 = models.CharField()
   image_3 = models.CharField()
   image_4 = models.CharField()

   images = [image_1, image_2, image_3, image_4]
   
   for x in range(4):
      images[x].blank = True and images[x] != image_1
      images[x].null = True and images[x] != image_1
      images[x].max_length = 255

   product = models.CharField(max_length=50) # Good max length

   price = models.CharField(max_length=15) # Good max length

   description = models.TextField(max_length=145, null=True, blank=True) # Good max length

   tags = models.TextField(max_length=500, null=True, blank=True)

   key = models.CharField(max_length=6, primary_key=True)

   def __str__(self):
      return f'{self.product} from {self.user.username}'




