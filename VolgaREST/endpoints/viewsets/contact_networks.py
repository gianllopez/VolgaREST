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
         urls = {
            'instagram': 'https://www.instagram.com/{}',
            'facebook': 'https://www.facebook.com/{}',
            'whatsapp': 'https://wa.me/{}',
            'twitter': 'https://www.twitter.com/{}',
            'email': 'mailto:{}',
            'linkedin': 'https://www.linkedin.com/in/{}'}
         return urls[network].format(contact)



         

         

         url = f'https://wa.me/{contact}' if network == 'whatsapp' else 'mailto:' + contact
         if network in ['facebook', 'instagram', 'twitter', 'linkedin']:
            cn = 'in/' + contact if network == 'linkedin' else contact
            url = f'https://www.{network}.com/{cn}'
         return url

   def create(self, request):
      data = request.data
      for field in data:
         data[field] = self.get_complete_url(field, data[field])
      data['user'] = request.__dict__['_user']
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(status=HTTP_201_CREATED)

