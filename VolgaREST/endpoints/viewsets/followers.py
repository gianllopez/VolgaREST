from VolgaREST.root.models.user import UserModel
from VolgaREST.root.models import FollowersModel
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_202_ACCEPTED
from ..custom import CreateViewSet

class FollowersViewSet(CreateViewSet):

   queryset = FollowersModel.objects.all()

   def create(self, request):
      user = UserModel.objects.get(username=request.data['user'])
      query = {'follower': request.user, 'user': user}
      follower = FollowersModel.objects.filter(**query)
      if follower.exists():
         follower.delete()
         response = {'data': {'following': False}, 'status': HTTP_202_ACCEPTED}
      else:
         FollowersModel.objects.create(**query)            
         response = {'data': {'following': True}, 'status': HTTP_201_CREATED}
      return Response(**response)
