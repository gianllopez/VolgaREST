from django.db import models
import os, binascii

# Create your models here.

class UserModel(models.Model):

   token = models.CharField(max_length=40, primary_key=True)

   name = models.CharField(max_length=65)
   
   username = models.CharField(
      max_length=25,
      unique=True,
      error_messages={'unique': 'Este nombre de usuario no está disponible.'})
   
   country = models.CharField(max_length=90)
   city = models.CharField(max_length=100)
 
   email = models.EmailField(
      max_length=125,
      unique=True,
      error_messages={'unique': 'Otra tienda usa este email.'})

   password = models.CharField(max_length=75)

   def save(self, *args, **kwargs):
      self.token = binascii.hexlify(os.urandom(20)).decode()
      self.name = self.name.capitalize().strip()
      self.username = self.username.lower().replace(' ', '')
      return super().save(*args, **kwargs)

   def __str__(self):
      return f'{self.owner} from {self.shop}'
