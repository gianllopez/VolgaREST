from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from ..serializers import LoginSerializer
from VolgaREST.root.models import UserModel
from .data_retrieve.formatter import ModelFormatter
from ..custom import CreateViewSet

class LoginViewSet(CreateViewSet):
   
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
            'picture': user.picture or ModelFormatter.blank_picture(user.gender)
         }, 'token': authtoken.key
      }, status=HTTP_200_OK)