from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ContactNetworksModel

class ContactNetworksSerializer(ModelSerializer):
   class Meta:
      model = ContactNetworksModel
      fields = '__all__'

   def get_complete_url(self, network, contact):
      if contact:
         if network in ['facebook', 'instagram', 'twitter', 'linkedin']:
            cn = 'in/' + contact if network == 'linkedin' else contact
            return f'https://www.{network}.com/{cn}'
         else:
            if network != 'user':
               return f'https://wa.me/{contact}' if network == 'whatsapp' else 'mailto:' + contact

   def create(self, validated_data):
      contact = {}
      for data in validated_data:
         if data != 'user':
            contact[data] = self.get_complete_url(data, validated_data[data])
      contact['user'] = validated_data['user']
      return ContactNetworksModel.objects.create(**contact)
