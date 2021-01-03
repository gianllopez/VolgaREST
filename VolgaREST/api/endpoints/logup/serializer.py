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
         'address',
         'foundation',
         'email',
         'password'
      ]
   
   def validate(self, data):
      shop = ShopModel.objects.filter(shop=data['shop'], owner=data['owner'])
      if shop.exists():
         raise ValidationError('Este propietario ya ha registrado esta tienda.')
      return data
