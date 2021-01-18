from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import UserTagsModel

class UserTagsSerializer(ModelSerializer):
   class Meta:
      model = UserTagsModel
      fields = '__all__'
