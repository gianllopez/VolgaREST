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

   def hostimages(self, images, username, product):
      toreturn = {}
      for img in images:
         if img[1]:
            imgid = '{}-{}-from-{}'.format(product.replace(' ', '-'), img[0], username)
            toreturn[img[0]] = upload (
               file=img[1],
               folder='products-images/',
               public_id=imgid
            )['secure_url']
      return toreturn

   def create(self, request):
      data = request.data
      data['user'] = request.__dict__['_user']
      images = self.hostimages (
         images=[(x, data[x]) for x in data if 'image_' in x],
         username=data['user'].username,
         product=data['product'])
      for x in data:
         if images.get(x, False) and 'image_' in x:
            data[x] = images[x]
      data['price'] = '{} {}'.format(data['price'], data['pricetype'])
      data['key'] = ''.join(choices(ascii_uppercase + digits, k=6))
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response (
         data={
            'user': data['user'].username,
            'key': data['key']
         }, status=HTTP_201_CREATED)
