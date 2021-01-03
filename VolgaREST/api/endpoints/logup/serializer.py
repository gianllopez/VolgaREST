from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from VolgaREST.root.models import ShopModel

class LogupSerializer(ModelSerializer):
   
   class Meta:
      model = ShopModel
      fields = [
         'owner',
         'shop',
         'country',
         'city',
         'address', # allow blank
         'foundation', # allow blank
         'email',
         'password'
      ]
      extra_kwargs = {}
      for field in fields:
         if field not in ['address', 'foundation']:
            extra_kwargs[field] = {
               'error_messages': {
                  'blank': 'Este campo es requerido.'
               }
            }
   
   def validate(self, data):
      shop = ShopModel.objects.filter(shop=data['shop'], owner=data['owner'])
      if shop.exists():
         raise ValidationError('Este propietario ya ha registrado esta tienda.')
      return data
