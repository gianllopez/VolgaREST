from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from ..serializers import ContactNetworksSerializer
from VolgaREST.root.models import ContactNetworksModel

class ContactNetworksViewSet(ModelViewSet):
   
   serializer_class = ContactNetworksSerializer
   queryset = ContactNetworksModel.objects.all()

   def create(self, request):
      request.data['user'] = request.__dict__['_user']
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(status=HTTP_201_CREATED)

