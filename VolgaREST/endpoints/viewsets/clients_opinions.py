from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from ..serializers import ClientsOpinionsSerializer
from VolgaREST.root.models import ClientsOpinionsModel, UserModel

class ClientOpinionsViewSet(ModelViewSet):

   serializer_class = ClientsOpinionsSerializer
   queryset = ClientsOpinionsModel.objects.all()

   def create(self, request):
      data, fromtoken = request.data, request.headers['Authorization'][6:]
      to_user, rating, comment = data['to_user'], data['rating'], data['comment']
      data['from_user'] = UserModel.objects.get(auth_token=fromtoken)
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(data={}, status=HTTP_200_OK)
      