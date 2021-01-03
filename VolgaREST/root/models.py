from django.db import models
import os, binascii

# Create your models here.

class ShopModel(models.Model):

   token = models.BinaryField(max_length=20, primary_key=True)

   owner = models.CharField(max_length=128)
   shop = models.CharField(max_length=25)
   country = models.CharField(max_length=90)
   city = models.CharField(max_length=100)
   address = models.CharField(max_length=95, blank=True, null=True)
   foundation = models.CharField(max_length=10, blank=True, null=True)
   email = models.EmailField(max_length=125, unique=True)
   password = models.CharField(max_length=75)

   def save(self, *args, **kwargs):
      self.token = binascii.hexlify(os.urandom(10)).decode()
      return super().save(*args, **kwargs)

   def __str__(self):
      return f'{self.owner} from {self.shop}'
