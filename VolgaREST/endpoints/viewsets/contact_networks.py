from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from ..serializers import ContactNetworksSerializer
from VolgaREST.root.models import ContactNetworksModel

class ContactNetworksViewSet(ModelViewSet):
   
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
      data['user'] = request.__dict__['_user']
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(status=HTTP_201_CREATED)

