from rest_framework.serializers import ModelSerializer
from VolgaREST.root.models import ContactModel, UserModel

class ContactSerializer(ModelSerializer):
   class Meta:
      model = ContactModel
      fields = '__all__'
