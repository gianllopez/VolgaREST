from django.contrib.auth.models import User
from VolgaREST.root.models.user import UserModel
from rest_framework.viewsets import ModelViewSet
from ..serializers import FollowersSerializer
from VolgaREST.root.models import FollowersModel
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND
from rest_framework.exceptions import ValidationError

class FollowersViewSet(ModelViewSet):
   
   serializer_class = FollowersSerializer
   queryset = FollowersModel.objects.all()

   def create(self, request):
      authtoken = request.headers['Authorization'][6:]
      follower = Token.objects.get(key=authtoken).user
      try:
         user = UserModel.objects.get(username=request.data['user'])
         query = {'follower': follower, 'user': user}
         follower = FollowersModel.objects.filter(**query)
         if follower.exists():
            follower.delete()
            response = {'data': {'action': 'remove'}, 'status': HTTP_202_ACCEPTED}
         else:
            request.data['follower'] = FollowersModel.objects.create(**query)            
            response = {'data': {'action': 'create'}, 'status': HTTP_201_CREATED}
         return Response(**response)
      except UserModel.DoesNotExist:
         return Response (
            data={request.data['user']: 'Este usuario no existe.'},
            status=HTTP_404_NOT_FOUND)
