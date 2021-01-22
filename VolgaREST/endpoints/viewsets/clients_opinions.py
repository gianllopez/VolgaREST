from rest_framework.viewsets import ModelViewSet
from ..serializers import ClientsOpinionsSerializer
from VolgaREST.root.models import ClientsOpinionsModel

class ClientOpinionsViewSet(ModelViewSet):
   serializer_class = ClientsOpinionsSerializer
   queryset = ClientsOpinionsModel.objects.all()
