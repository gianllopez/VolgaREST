from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from VolgaREST.root.models import UserModel
from cloudinary.uploader import upload
from ..custom import CreateViewSet

class UserProfilePictureViewSet(CreateViewSet):
   
   queryset = UserModel.objects.all()

   def create(self, request):
      loadedpic = request.data['picture']
      user = request.user
      response = {'status': HTTP_201_CREATED}
      if loadedpic:
         id = f'{user.username}-profile-picture'
         config = {
            'file': loadedpic.file,
            'folder': f'users-assets/{user.username}',
            'public_id': 'profile-picture'
         }
         user.picture = upload(**config)['secure_url']
         user.save()
         response['data'] = {'username': user.username, 'picture': user.picture}
      return Response(**response)
