from rest_framework.serializers import Serializer, CharField
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from VolgaREST.root.models import UserModel

class LoginSerializer(Serializer):

   username = CharField(max_length=75)
   password = CharField(max_length=50)

   def validate(self, data):
      user = authenticate(**data)
      if not user:
         raise ValidationError({'auth-error': 'Credenciales incorrectas.'})
      return data
