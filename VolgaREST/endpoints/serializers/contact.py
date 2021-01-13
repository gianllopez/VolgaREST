from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ContactModel, UserModel
from ..utils.contact_auth import ContactAuthentication

class ContactSerializer(ModelSerializer):
   
   class Meta:
      model = ContactModel
      fields = '__all__'
   
   def validate(self, data):
      # import pdb; pdb.set_trace()
      contacts = {}
      for x in data:
         if x not in ['token', 'whatsapp']:
            contacts[x] = data[x]
      auth = ContactAuthentication(credentials=contacts)
      auth.execute()
      return data