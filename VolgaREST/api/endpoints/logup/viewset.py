from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .serializer import LogupSerializer, ShopModel

class LogupViewSet(ModelViewSet):
   
   serializer_class = LogupSerializer
   queryset = ShopModel.objects.all()

   def create(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      shop = serializer.save()
      data = {
         'data': {
            'owner': shop.owner,
            'shop': shop.shop
         },
         'token': shop.token
      }
      return Response(data, status=HTTP_201_CREATED)
