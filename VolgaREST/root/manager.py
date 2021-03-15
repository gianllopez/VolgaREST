from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

   def create_user(self, username, password):
      user = self.model(username=username, password=password)
      # user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, username, password):
      user = self.create_user(username=username, password=password)
      user.set_password(password)
      user.is_superuser = True
      user.save(using=self._db)
      return user