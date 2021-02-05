from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import FollowersModel

class FollowersSerializer(ModelSerializer):
   class Meta:
      model = FollowersModel
      fields = '__all__'