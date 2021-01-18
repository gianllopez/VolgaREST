from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authtoken.models import Token
from ..serializers import LogupSerializer
from VolgaREST.root.models import UserModel

class LogupViewSet(ModelViewSet):
   
   serializer_class = LogupSerializer
   queryset = UserModel.objects.all()

   def create(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.save()
      authtoken = Token.objects.create(user=user)
      return Response(
         data={
            'credentials': {
               'username': user.username,
               'password': user.password
            },
            'token': authtoken.key
         },
         status=HTTP_201_CREATED)
