from django.contrib.auth.models import User
from VolgaREST.root.models.user import UserModel
from rest_framework.viewsets import ModelViewSet
from VolgaREST.root.models import FollowersModel
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED

class FollowersViewSet(ModelViewSet):

   queryset = FollowersModel.objects.all()

   def create(self, request):
      follower = request.__dict__['_user']
      user = UserModel.objects.get(username=request.data['user'])
      query = {'follower': follower, 'user': user}
      follower = FollowersModel.objects.filter(**query)
      if follower.exists():
         follower.delete()
         response = {'data': {'following': False}, 'status': HTTP_202_ACCEPTED}
      else:
         FollowersModel.objects.create(**query)            
         response = {'data': {'following': True}, 'status': HTTP_201_CREATED}
      return Response(**response)
