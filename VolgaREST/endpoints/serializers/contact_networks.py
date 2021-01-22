from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ContactNetworksModel

class ContactNetworksSerializer(ModelSerializer):
   class Meta:
      model = ContactNetworksModel
      fields = '__all__'
