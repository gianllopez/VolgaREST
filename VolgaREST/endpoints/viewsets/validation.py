from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet
from VolgaREST.root.models import UserModel
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class ValidationViewSet(GenericViewSet):
   
   queryset = UserModel.objects.all()

   @action(methods=['post'], detail=False, url_path='user-exists')
   def user_exists(self, request):
      username = request.data.get('username', None)
      response = {'status': HTTP_404_NOT_FOUND}
      if username:
         user = UserModel.objects.filter(username=username)
         if user.exists():
            response['status'] = HTTP_200_OK
      return Response(**response)
