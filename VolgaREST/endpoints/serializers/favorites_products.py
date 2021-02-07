from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import FavoritesProducts

class FavoritesProductsSerializer(ModelSerializer):
   class Meta:
      model = FavoritesProducts
      fields = '__all__'
