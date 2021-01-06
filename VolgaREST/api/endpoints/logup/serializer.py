from rest_framework.serializers import ModelSerializer
from rest_framework.validators import ValidationError
from VolgaREST.root.models import ShopModel
from re import match

class LogupSerializer(ModelSerializer):
   
   class Meta:
      model = ShopModel
      fields = [
         'name',
         'username',
         'country',
         'city',
         'email',
         'password'
      ]
      extra_kwargs = {}
      for field in fields:
         extra_kwargs[field] = {
            'error_messages': {
               'blank': 'Este campo es requerido.'
            }
         }
   
   def regex_validator(self, data, to_valid):
      errors = {}
      errormsg = 'El formato es incorrecto.'
      for x in data:
         if not match(data[x], to_valid[x]):
            errors[x] = errormsg
      return errors

   
   def validate(self, data):
      import pdb; pdb.set_trace()
      to_valid = {
         'name': r'(?!.*\s{2})^[a-zA-ZÀ-úñÑ\s]+$',
         'username': r'^[a-z0-9]*$'
      }
      errors = self.regex_validator(data, to_valid)
      if errors:
         raise ValidationError(errors)
