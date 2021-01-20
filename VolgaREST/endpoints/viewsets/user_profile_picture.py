from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from ..serializers import UserProfilePictureSerializer
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload

class UserProfilePictureViewSet(GenericViewSet, CreateModelMixin):
   serializer_class = UserProfilePictureSerializer
   queryset = UserModel.objects.all()

   def get_blankpp(self, gender):
         genderspp = {
            'Masculino': 'blankpp-men.png',
            'Masculino': 'blankpp-women.png',
            'No definido': 'blankpp-undefined.png',
            'Prefiero no especificarlo': 'blankpp-undefined.png'
         }
         baseurl = 'https://res.cloudinary.com/volga/image/upload/v1611089503/'
         return baseurl + genderspp[gender]
         
   def create(self, request):
      username, loadedpic = request.data.values()
      user = UserModel.objects.get(username=username)
      if loadedpic:
         picture = upload (
            file=loadedpic.file, folder='profile-pictures/',
            public_id=username, overwrite=True)
         user.picture = picture['secure_url']
      else:
         user.picture = self.get_blankpp(gender=user.gender)
      user.save()
      return Response(data={'profile-picture': user.picture}, status=HTTP_201_CREATED)