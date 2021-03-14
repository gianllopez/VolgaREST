from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from VolgaREST.root.models import UserModel
from re import match

class LogupSerializer(ModelSerializer):
   class Meta:
      model = UserModel
      exclude = ['picture']