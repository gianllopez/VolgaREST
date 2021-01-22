from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ClientsOpinionsModel

class ClientsOpinionsSerializer(ModelSerializer):
   class Meta:
      model = ClientsOpinionsModel
      fields = '__all__'
