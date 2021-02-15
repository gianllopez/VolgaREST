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

   def create(self, request):
      username, loadedpic = request.data['username'], request.data['picture']
      user = UserModel.objects.get(username=username)
      if loadedpic:
         picture = upload (
            file=loadedpic.file, folder='profile-pictures/',
            public_id=username, overwrite=True)['secure_url']
         user.picture = picture
      user.save()
      return Response(data={'profile-picture': user.picture}, status=HTTP_201_CREATED)