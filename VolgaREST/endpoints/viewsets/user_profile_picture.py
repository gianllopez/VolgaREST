from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from ..serializers import UserProfilePictureSerializer
from VolgaREST.root.models import UserModel

class UserProfilePictureViewSet(GenericViewSet, CreateModelMixin):
   serializer_class = UserProfilePictureSerializer
   queryset = UserModel.objects.all()
