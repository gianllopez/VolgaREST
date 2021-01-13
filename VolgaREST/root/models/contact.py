from django.db import models
from .user import UserModel

class ContactModel(models.Model):

   token = models.OneToOneField(
      to=UserModel,
      primary_key=True,
      on_delete=models.CASCADE,
      error_messages={'unique': 'Este usuario ya añadió sus redes de contacto.'})
   
   unique_error = {'unique': 'Otro usuario ya registró esta cuenta.'}

   instagram = models.CharField(max_length=30, error_messages=unique_error)
   facebook = models.CharField(max_length=50, error_messages=unique_error)
   whatsapp = models.CharField(max_length=15, error_messages=unique_error)
   twitter = models.CharField(max_length=15, error_messages=unique_error)
   email = models.CharField(max_length=100, error_messages=unique_error)

   fields = [instagram, facebook, whatsapp, twitter, email]
   for x in range(len(fields)):
      fields[x]._unique = True
      fields[x].blank = True
      fields[x].null = True
   
   def __str__(self):
      return self.user.username