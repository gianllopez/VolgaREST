from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from ..serializers import ClientsOpinionsSerializer
from VolgaREST.root.models import ClientsOpinionsModel
from ..custom import CreateViewSet

class ClientOpinionsViewSet(CreateViewSet):

   serializer_class = ClientsOpinionsSerializer
   queryset = ClientsOpinionsModel.objects.all()

   def create(self, request):
      request.data['from_user'] = request.user
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(status=HTTP_201_CREATED)