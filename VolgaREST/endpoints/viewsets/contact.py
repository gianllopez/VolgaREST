from rest_framework.viewsets import ModelViewSet
from ..serializers import ContactSerializer
from VolgaREST.root.models import ContactModel

class ContactViewSet(ModelViewSet):
   serializer_class = ContactSerializer
   queryset = ContactModel.objects.all()
