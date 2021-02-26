from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from ..serializers import ClientsOpinionsSerializer
from VolgaREST.root.models import ClientsOpinionsModel, UserModel
from . import CreateViewSet

class ClientOpinionsViewSet(CreateViewSet):

   serializer_class = ClientsOpinionsSerializer
   queryset = ClientsOpinionsModel.objects.all()

   def create(self, request):
      request.data['from_user'] = request.__dict__['_user']
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(status=HTTP_201_CREATED)