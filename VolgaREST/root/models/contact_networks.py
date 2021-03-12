from django.db import models
from .user import UserModel

class ContactNetworksModel(models.Model):

   user = models.OneToOneField(
      to=UserModel,
      primary_key=True,
      on_delete=models.CASCADE,
      error_messages={'unique': 'Este usuario ya añadió sus redes de contacto.'})
   
   unique_error = {'unique': 'Otro usuario ya registró esta cuenta.'}

   instagram = models.CharField(max_length=56, error_messages=unique_error)
   facebook = models.CharField(max_length=75, error_messages=unique_error)
   whatsapp = models.CharField(max_length=40, error_messages=unique_error)
   twitter = models.CharField(max_length=40, error_messages=unique_error)
   linkedin = models.CharField(max_length=50, error_messages=unique_error) # max_length=60
   email = models.EmailField(max_length=110, error_messages=unique_error)

   fields = [instagram, facebook, whatsapp, twitter, linkedin, email]
   for x in range(6):
      fields[x]._unique = True
      fields[x].blank = True
      fields[x].null = True
   
   def __str__(self):
      return self.user.username
