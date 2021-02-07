from django.db import models
from .user import UserModel

class ClientsOpinionsModel(models.Model):

   from_user = models.ForeignKey (
      to=UserModel,
      on_delete=models.CASCADE,
      related_name='from_user')
   
   to_user = models.ForeignKey (
      to=UserModel,
      on_delete=models.CASCADE,
      related_name='to_user')

   rating = models.FloatField(default=10)
   comment = models.TextField(max_length=125)

   date = models.DateField(auto_now_add=True)

   def __str__(self):
      return self.from_user.username