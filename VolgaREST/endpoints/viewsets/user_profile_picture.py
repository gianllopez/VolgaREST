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
         id = f'{user.username}-profile-picture'
         config = {
            'file': loadedpic.file,
            'folder': f'users-assets/{user.username}',
            'public_id': 'profile-picture'
         }
         user.picture = upload(**config)['secure_url']
         user.save()
      return Response(status=HTTP_201_CREATED)
