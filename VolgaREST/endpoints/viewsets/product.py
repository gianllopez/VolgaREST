from rest_framework.viewsets import ModelViewSet
from ..serializers import NewProductSerializer
from VolgaREST.root.models import ProductModel
from cloudinary.uploader import upload

class NewProductViewSet(ModelViewSet):
   
   serializer_class = NewProductSerializer
   queryset = ProductModel.objects.all()

   def imgs_to_url(self, reqdata):
      imgfields = [f'image_{x}' for x in range(1, 5)]
      for data in reqdata:
         if data in imgfields:
            name = reqdata['product'] + '-' + str(imgfields.index(data))
            reqdata[data] = upload (
               file=reqdata[data], folder='products/',
               public_id=name, overwrite=True).get('secure_url')
      return reqdata

   def create(self, request):
      data = self.imgs_to_url(reqdata=request.data)
      serializer = self.serializer_class(data=data)
      
            

      