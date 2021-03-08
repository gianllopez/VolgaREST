from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from ..serializers import NewProductSerializer
from VolgaREST.root.models import ProductModel
from cloudinary.uploader import upload, destroy
from ..custom import CreateViewSet
from os.path import splitext
from cloudinary.api import delete_folder
from random import choices
from string import ascii_uppercase, digits

class ProductsViewSet(CreateViewSet):
   
   serializer_class = NewProductSerializer
   queryset = ProductModel.objects.all()

   def host_delete(self, username, images, key):
      folder = 'users-assets/{}/products/{}/'.format(username, key)
      for img in images:
         img_id = img.split('/')[-1]
         destroy(public_id=folder + splitext(img_id)[0])
      delete_folder(folder)

   @action(methods=['post'], detail=False)
   def new(self, request):
      data = request.data
      data['user'] = request.__dict__['_user']
      data['price'] = '{} {}'.format(data['price'], data.pop('pricetype')[0])
      data['key'] = ''.join(choices(ascii_uppercase + digits, k=10))
      username = data['user'].username
      images = request.FILES.getlist('images')
      FOLDER = 'users-assets/{}/products/'.format(username)
      urls = []
      for img in images:
         config = {
            'file': img.file,
            'public_id': splitext(img.name)[0],
            'folder': FOLDER + data['key']}
         urls.append(upload(**config)['secure_url'])
      data['images'] = ', '.join(urls)
      serializer = self.serializer_class(data=data)
      serializer.is_valid(raise_exception=True)
      product = serializer.save()
      return Response(data={
         'username': username,
         'key': product.key}, status=HTTP_201_CREATED)
   
   @action(methods=['post'], detail=False)
   def delete(self, request):
      to_delete = ProductModel.objects.filter(**request.data)
      if to_delete.exists():
         to_delete = to_delete.first()
         delete_conf = {
            'username': request.user.username,
            'images': to_delete.images.split(','),
            'key': to_delete.key}
         self.host_delete(**delete_conf)
         to_delete.delete()
      return Response(status=HTTP_204_NO_CONTENT)
