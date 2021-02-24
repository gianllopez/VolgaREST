from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from ..serializers import NewProductSerializer
from VolgaREST.root.models import ProductModel
from cloudinary.uploader import upload, destroy
from random import choices
from string import ascii_uppercase, digits

class ProductsViewSet(GenericViewSet):
   
   serializer_class = NewProductSerializer
   queryset = ProductModel.objects.all()

   @action(methods=['post'], detail=False)
   def new(self, request):
      data = request.data
      data['user'] = request.__dict__['_user']
      username = data['user'].username
      images = request.FILES.getlist('images')
      FOLDER = 'users-assets/{}/products/'.format(username)
      urls = []
      for img in images:
         config = {
            'file': img.file,
            'public_id': img.name,
            'folder': FOLDER + data['product']}
         urls.append(upload(**config)['secure_url'])
      data['images'] = ', '.join(urls)
      data['price'] = '{} {}'.format(data['price'], data.pop('pricetype')[0])
      data['key'] = ''.join(choices(ascii_uppercase + digits, k=10))
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      product = serializer.save()
      return Response(data={
         'username': username,
         'key': product.key}, status=HTTP_201_CREATED)
   
   @action(methods=['post'], detail=False)
   def delete(self, request):
      ProductModel.objects.filter(**request.data).delete()
      # destroy()
      return Response(status=HTTP_204_NO_CONTENT)
      
      
