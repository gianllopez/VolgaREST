from rest_framework.viewsets import GenericViewSet
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload

class UserProfilePictureViewSet(GenericViewSet):
   
   queryset = UserModel.objects.all()

   def create(self, request):
      loadedpic = request.data['picture']
      user = request.__dict__['_user']
      if loadedpic:
         picture = upload (
            file=loadedpic.file, folder='profile-pictures/',
            public_id=user.username, overwrite=True)
         user.picture = picture['secure_url']
      user.save()
      return Response(status=HTTP_201_CREATED)