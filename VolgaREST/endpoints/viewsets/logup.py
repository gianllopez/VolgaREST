from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authtoken.models import Token
from ..serializers import LogupSerializer
from VolgaREST.root.models import UserModel
from .data_retrieve.formatter import ModelFormatter
from ..custom import CreateViewSet

class LogupViewSet(CreateViewSet):
   
   serializer_class = LogupSerializer
   queryset = UserModel.objects.all()
   authentication_classes = permission_classes = []

   def create(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      authtoken = Token.objects.create(user=user)
      return Response(data={
         'uiprev': {
            'username': user.username,
            'picture': user.picture or ModelFormatter.blank_picture(user.gender)
         }, 'token': authtoken.key
      }, status=HTTP_201_CREATED)
