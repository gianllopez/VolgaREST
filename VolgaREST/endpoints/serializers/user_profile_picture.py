from rest_framework.serializers import Serializer, CharField, ImageField
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload

class UserProfilePictureSerializer(Serializer):
   
   username = CharField(max_length=25)
   picture = ImageField(allow_empty_file=True)

   def create(self, validated_data):
      username, picture = validated_data.values()
      picture = upload(
         file=picture.file, folder='profile-pictures/',
         public_id=username, overwrite=True)
      user = UserModel.objects.get(username=username)
      user.picture = picture['secure_url']
      user.save()
      return validated_data
