from django.contrib.auth.models import User
from django.db import models
from .user import UserModel

class FollowersModel(models.Model):
   
   user = models.ForeignKey(
      to=UserModel, on_delete=models.CASCADE,
      related_name='user'
   )
   
   follower = models.ForeignKey(
      to=UserModel, on_delete=models.CASCADE,
      related_name='follower'
   )
   
   def __str__(self):
       return self.user.username
