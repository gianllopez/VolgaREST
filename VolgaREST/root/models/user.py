from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserModel(AbstractBaseUser):

   name = models.CharField(max_length=65)
   
   picture = models.CharField(max_length=256, blank=True, null=True)

   username = models.CharField(
      max_length=25,
      primary_key=True,
      error_messages={'unique': 'Este nombre de usuario ya fue tomado.'})
   
   country = models.CharField(max_length=90)
   city = models.CharField(max_length=100)

   gender = models.CharField(max_length=20)

   email = models.EmailField(
      max_length=125,
      unique=True,
      error_messages={'unique': 'Otro usuario usa este correo.'})
   
   email_code = models.IntegerField(default=0)

   verified_email = models.BooleanField(default=False, blank=True, null=True)

   USERNAME_FIELD = 'username'
   objects = BaseUserManager()
   last_login = None

   def save(self, *args, **kwargs):
      self.name = self.name.title()
      self.username = self.username.lower()
      self.country = self.country.title()
      self.city = self.city.title()
      return super().save(*args, **kwargs)

   def __str__(self):
      return self.username
