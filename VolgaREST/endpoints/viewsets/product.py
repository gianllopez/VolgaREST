from rest_framework.viewsets import ModelViewSet
from ..serializers import NewProductSerializer
from VolgaREST.root.models import ProductModel

class NewProductViewSet(ModelViewSet):
   serializer_class = NewProductSerializer
   queryset = ProductModel.objects.all()