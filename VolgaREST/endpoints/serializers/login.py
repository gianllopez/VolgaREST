from rest_framework.serializers import Serializer, CharField
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from VolgaREST.root.models import UserModel

class LoginSerializer(Serializer):

   username = CharField(max_length=75)
   password = CharField(max_length=50)

   def validate(self, data):
      self.user = UserModel.objects.filter(**data)
      if not self.user.exists():
         raise ValidationError({'password': 'Nombre de usuario y/o contraseña incorrecto(s).'})
      return data
   
   def create(self, validated_data):
      return Token.objects.get(user=self.user.first())
