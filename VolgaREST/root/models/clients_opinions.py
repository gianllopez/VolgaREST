from django.db import models
from .user import UserModel

class ClientsOpinionsModel(models.Model):

   user = models.ForeignKey (
      to=UserModel,
      on_delete=models.CASCADE)

   rating = models.IntegerField(default=10)
   client = models.CharField(max_length=75)
   email = models.EmailField(max_length=100)
   comment = models.TextField(max_length=125)

   def __str__(self):
      return self.user