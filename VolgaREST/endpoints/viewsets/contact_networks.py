from rest_framework.viewsets import ModelViewSet
from ..serializers import ContactNetworksSerializer
from VolgaREST.root.models import ContactNetworksModel

class ContactNetworksViewSet(ModelViewSet):
   serializer_class = ContactNetworksSerializer
   queryset = ContactNetworksModel.objects.all()
