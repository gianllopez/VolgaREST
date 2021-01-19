from rest_framework.serializers import Serializer, CharField, ImageField
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload

class UserProfilePictureSerializer(Serializer):
   
   username = CharField(max_length=25)
   picture = ImageField(allow_empty_file=True)

   def create(self, validated_data):
      username, loadedpic = validated_data.values()
      user = UserModel.objects.get(username=username)
      if loadedpic:
         picture = upload(
            file=loadedpic.file, folder='profile-pictures/',
            public_id=username, overwrite=True)
         user.picture = picture['secure_url']
         user.save()
      else:
         baseurl = 'https://res.cloudinary.com/volga/image/upload/v1611089503/blankpp-'
         loadedpic = baseurl + 
      return validated_data
