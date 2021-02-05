from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ClientsOpinionsModel

class ClientsOpinionsSerializer(ModelSerializer):
   class Meta:
      model = ClientsOpinionsModel
      fields = [
         'from_user',
         'to_user',
         'rating',
         'comment'
      ]
