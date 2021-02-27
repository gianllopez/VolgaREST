from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT
from ..serializers import ContactNetworksSerializer
from VolgaREST.root.models import ContactNetworksModel
from ..custom import CreateViewSet

class ContactNetworksViewSet(CreateViewSet):
   
   serializer_class = ContactNetworksSerializer
   queryset = ContactNetworksModel.objects.all()

   def get_complete_url(self, network, contact):
      if contact:
         c_urls = ['instagram', 'facebook', 'twitter']
         urls = {a: 'https://www.{}.com/'.format(b) + '{}' for (a, b) in zip(c_urls, c_urls)}
         urls['whatsapp'] = 'https://wa.me/{}'
         urls['linkedin'] = 'https://www.linkedin.com/in/{}' 
         return urls[network].format(contact)

   def create(self, request):
      data = request.data
      for field in data:
         if field != 'email':
            data[field] = self.get_complete_url(field, data[field])
      data['user'] = request.user
      serializer = self.serializer_class(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response(status=HTTP_201_CREATED)
      else:
         return Response(data=serializer.errors, status=HTTP_409_CONFLICT)

