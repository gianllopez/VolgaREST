from django.db.models import CharField, EmailField
from django.contrib.auth.models import AbstractBaseUser

class UserModel(AbstractBaseUser):

   name = CharField(max_length=65)
   
   username = CharField(
      max_length=25,
      primary_key=True,
      error_messages={'unique': 'Este nombre de usuario ya fue tomado.'})
   
   country = CharField(max_length=90)
   city = CharField(max_length=100)
 
   email = EmailField(
      max_length=125,
      unique=True,
      error_messages={'unique': 'Otro usuario usa este correo.'})

   USERNAME_FIELD = 'username'
   last_login = None

   def save(self, *args, **kwargs):
      self.name = self.name.title().strip()
      self.username = self.username.lower().replace(' ', '')
      return super().save(*args, **kwargs)

   def __str__(self):
      return f'{self.username}'
