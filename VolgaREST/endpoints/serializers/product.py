from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ProductModel

class NewProductSerializer(ModelSerializer):
   class Meta:
      model = ProductModel
      fields = [
         'user',
         'image_1',
         'image_2',
         'image_3 ',
         'image_4',
         'product ',
         'price ',
         'description '
      ]