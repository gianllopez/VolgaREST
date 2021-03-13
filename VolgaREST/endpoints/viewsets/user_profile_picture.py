from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.response import Response
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload
from ..custom import CreateViewSet

class UserProfilePictureViewSet(CreateViewSet):
   
   queryset = UserModel.objects.all()

   def create(self, request):
      loadedpic = request.data['picture']
      user = request.user
      response = {'status': HTTP_200_OK}
      if loadedpic:
         config = {
            'file': loadedpic.file,
            'folder': f'users-assets/{user.username}',
            'public_id': 'profile-picture'
         }
         user.picture = upload(**config)['secure_url']
         user.save()
         response = {
            'data': {               
               'username': user.name,
               'picture': user.picture
            }, 'status': HTTP_201_CREATED
         }
      return Response(**response)
