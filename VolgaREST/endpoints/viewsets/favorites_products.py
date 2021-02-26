from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from ..serializers import FavoritesProductsSerializer
from VolgaREST.root.models import FavoritesProducts
from ..custom import CreateViewSet

class FavoritesProductsViewSet(CreateViewSet):
   
   serializer_class = FavoritesProductsSerializer
   queryset = FavoritesProducts.objects.all()

   def create(self, request):
      request.data['user'] = request.__dict__['_user']
      isfav = FavoritesProducts.objects.filter(**request.data)
      if isfav.exists():
         isfav.first().delete()
         response = {'data': {'isfav': False}, 'status': HTTP_200_OK}
      else:
         serializer = self.serializer_class(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         response = {'data': {'isfav': True}, 'status': HTTP_201_CREATED}
      return Response(**response)
      