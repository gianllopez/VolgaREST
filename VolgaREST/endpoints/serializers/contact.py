from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ContactModel, UserModel
from ..utils.contact_auth import ContactAuthentication

class ContactSerializer(ModelSerializer):
   
   class Meta:
      model = ContactModel
      fields = '__all__'
   
   def validate(self, data):
      auth = ContactAuthentication()
      contacts = {}
      for x in data:
         if x != 'token':
            contacts[x] = data[x]
      import pdb; pdb.set_trace()
