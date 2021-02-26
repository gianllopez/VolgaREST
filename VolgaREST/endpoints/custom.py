from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

class CreateViewSet(GenericViewSet, CreateModelMixin):
   pass