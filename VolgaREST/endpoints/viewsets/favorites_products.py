from rest_framework.viewsets import ModelViewSet
from ..serializers import FavoritesProductsSerializer
from VolgaREST.root.models import FavoritesProducts,ProductModel

class FavoritesProductsViewSet(ModelViewSet):
   
   serializer_class = FavoritesProductsSerializer
   queryset = FavoritesProducts.objects.all()

   def create(self, request):
      productkey = request.data['productkey']
      product = ProductModel.objects.get(key=productkey)
      user = request.__dict__['_user']
      import pdb; pdb.set_trace()