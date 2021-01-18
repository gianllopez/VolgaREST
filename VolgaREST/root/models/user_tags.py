from django.db import models
from .user import UserModel

class UserTagsModel(models.Model):
   user = models.OneToOneField(
      to=UserModel,
      on_delete=models.CASCADE,
      primary_key=True,
      error_messages={'unique': 'Este usuario ya añadió sus etiquetas.'})
   tags = models.CharField(max_length=400, null=True, blank=True)
   
   def __str__(self):
      return self.user
