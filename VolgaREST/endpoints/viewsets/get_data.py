from rest_framework import response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from django.forms.models import model_to_dict
from VolgaREST.root.models import UserModel, ProductModel

class GetDataViewSet(GenericViewSet):

   queryset = UserModel.objects.all()

   @action(methods=['get'], detail=False)
   def product(self, request):
      params = request.GET
      username, productkey = params['username'], params['productkey']
      result = ProductModel.objects.filter(user=username, key=productkey)
      if not result.exists():
         raise ValidationError({'error': 404})
      else:
         product = model_to_dict(result.first())
         response = {}
         response['images'] = [product[x] for x in product if 'image_' in x]
         for data in product:
            if 'image_' not in data and data != 'id':
               response[data] = product[data]
         return Response(data=response, status=HTTP_200_OK)
      
   @action(methods=['get'], detail=False)
   def user(self, request):
      username = request.GET['username']
      user = UserModel.objects.get(username=username)
      import pdb; pdb.set_trace()
