from rest_framework.viewsets import ModelViewSet
from .serializer import LogupSerializer, ShopModel

class LogupViewSet(ModelViewSet):
   serializer_class = LogupSerializer
   queryset = ShopModel.objects.all()
