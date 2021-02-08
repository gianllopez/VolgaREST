from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet
from VolgaREST.root.models import UserModel, user
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class ValidationViewSet(GenericViewSet):
   
   queryset = UserModel.objects.all()

   @action(methods=['post'], detail=False, url_path='user-exists')
   def user_exists(self, request):
      username = request.data.get('username', None)
      if username and username != 'me':
         user = UserModel.objects.filter(username=username)
         return Response (
            status=HTTP_200_OK if user.exists() else HTTP_404_NOT_FOUND)
      else:
         raise ValidationError({'username': 'Este parámetro es requerido.'})
