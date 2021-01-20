from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import UserModel

class UserProfilePictureSerializer(ModelSerializer):
   class Meta:
      model = UserModel
      fields = [
         'username',
         'picture'
      ]


