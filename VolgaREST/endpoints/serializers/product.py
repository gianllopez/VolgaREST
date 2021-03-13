from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ProductModel

class NewProductSerializer(ModelSerializer):
   class Meta:
      model = ProductModel
      fields = '__all__'
