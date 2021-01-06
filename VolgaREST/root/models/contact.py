from django.db import models
from .user import UserModel

class ContactModel(models.Model):

   user = models.OneToOneField(
      to=UserModel,
      primary_key=True,
      on_delete=models.CASCADE)

   instagram = models.CharField(max_length=30)
   facebook = models.CharField(max_length=50)
   whatsapp = models.CharField(max_length=15)
   twitter = models.CharField(max_length=15)
   email = models.CharField(max_length=100)

   fields = [instagram, facebook, whatsapp, twitter, email]
   for x in range(len(fields)):
      fields[x]._unique = True
      fields[x].blank = True
      fields[x].null = True
      fields[x]._error_messages = {'unique': 'Otro usuario ya registró esta cuenta.'}

   def __str__(self):
      return self.user.name