import re
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ..serializers import LoginSerializer
from VolgaREST.root.models import UserModel

class LoginViewSet(ViewSet):
   
   serializer_class = LoginSerializer
   queryset = UserModel.objects.all()
   authentication_classes = permission_classes = []

   def create(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      authtoken = serializer.save()
      user = authtoken.user
      return Response(data={
         'uiconstdata': {
            'username': user.username,
            'picture': user.picture
         },
         'token': authtoken.key
      }, status=HTTP_200_OK)