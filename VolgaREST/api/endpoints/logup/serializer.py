from rest_framework.serializers import ModelSerializer
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
