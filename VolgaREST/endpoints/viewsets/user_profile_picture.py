from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload

class UserProfilePictureViewSet(GenericViewSet, CreateModelMixin):
   
   queryset = UserModel.objects.all()

   def create(self, request):
      loadedpic = request.data['picture']
      user = request.__dict__['_user']
      if loadedpic:
         picture = upload (
            file=loadedpic.file, folder='profile-pictures/',
            public_id=user.username, overwrite=True)['secure_url']
         user.picture = picture
      user.save()
      return Response(data={'profile-picture': user.picture}, status=HTTP_201_CREATED)