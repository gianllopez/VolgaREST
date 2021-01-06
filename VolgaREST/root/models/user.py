from django.db import models
import os, binascii

class UserModel(models.Model):

   token = models.CharField(max_length=40, primary_key=True)

   name = models.CharField(max_length=65)
   
   username = models.CharField(
      max_length=25,
      unique=True,
      error_messages={'unique': 'Este nombre de usuario ya fue tomado.'})
   
   country = models.CharField(max_length=90)
   city = models.CharField(max_length=100)
 
   email = models.EmailField(
      max_length=125,
      unique=True,
      error_messages={'unique': 'Otro usuario usa este correo.'})

   password = models.CharField(max_length=75)

   def save(self, *args, **kwargs):
      self.token = binascii.hexlify(os.urandom(20)).decode()
      self.name = self.name.title().strip()
      self.username = self.username.lower().replace(' ', '')
      return super().save(*args, **kwargs)

   def __str__(self):
      return f'{self.username}'
