from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from ..serializers import NewProductSerializer
from VolgaREST.root.models import ProductModel, UserModel
from cloudinary.uploader import upload
from random import choices
from string import ascii_uppercase, digits

class NewProductViewSet(ModelViewSet):
   
   serializer_class = NewProductSerializer
   queryset = ProductModel.objects.all()

   def imgs_to_url(self, reqdata):
      imgfields = [f'image_{x}' for x in range(1, 5)]
      for data in reqdata:
         if data in imgfields:
            user, product, index = reqdata['user'], reqdata['product'], imgfields.index(data)
            name = f'{product}({index})-from-{user}'
            if reqdata[data]:
               reqdata[data] = upload (
                  file=reqdata[data], folder='products/',
                  public_id=name, overwrite=True).get('secure_url')
      return reqdata

   def create(self, request):
      data = self.imgs_to_url(reqdata=request.data)
      user, price, pricetype = data['user'], data['price'], data['pricetype']
      data['user'] = UserModel.objects.get(username=user)
      data['price'] = f'{price} {pricetype}'
      data['key'] = ''.join(choices(ascii_uppercase + digits, k=6))
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response (data=serializer.data, status=HTTP_201_CREATED)
      
            

      