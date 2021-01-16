from rest_framework.viewsets import ModelViewSet
from ..serializers import UserTagsSerializer
from VolgaREST.root.models import UserTagsModel

class UserTagsViewSet(ModelViewSet):
   serializer_class = UserTagsSerializer
   queryset = UserTagsModel.objects.all()
