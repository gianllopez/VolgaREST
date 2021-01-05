from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from VolgaREST.root.models import ShopModel

class LogupSerializer(ModelSerializer):
   
   class Meta:
      model = ShopModel
      fields = [
         'name',
         'username',
         'country',
         'city',
         'email',
         'password'
      ]
      extra_kwargs = {}
      for field in fields:
         extra_kwargs[field] = {
            'error_messages': {
               'blank': 'Este campo es requerido.'
            }
         }
