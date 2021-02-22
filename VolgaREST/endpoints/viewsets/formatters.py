from django.forms import model_to_dict

class ModelFormatter:


   def fields_filter(self, instance, filter=[], reverse=False):
      instance_dict = model_to_dict(instance)
      filter_result = {}
      for data in instance_dict:
         infilter = data in filter
         if reverse and not infilter:
            filter_result[data] = instance_dict[data]
         if not reverse and infilter:
            filter_result[data] = instance_dict[data]
      return filter_result

   def user(self, user_instance):
      return self.fields_filter(
            instance=product_instance.user,
            filter=['username', 'name', 'picture'])
   
   def product(self, product_instance, include_user=False):
      product_data = self.fields_filter(product_instance, ['user'], True)
      product_response = {'images': []}
      for prodata in product_data:
         value = product_data[prodata]
         isimg = 'image_' in prodata
         if value:
            if isimg:
               product_response['images'].append(value)
            else:
               product_response[prodata] = value
      if tags := product_response.get('tags', None):
         tags = tags.split(', ')
      if include_user:
         product_response['user'] = self.user(product_instance.user)
      return product_response

   # def product(self, request): 
   #    result = ProductModel.objects.filter(user=username, key=productkey)
   #    if not result.exists():
   #       raise ValidationError({'error': 404})
   #    else:
   #       product_result = result.first()
   #       product = model_to_dict(product_result)
   #       response = {}
   #       response['images'] = [product[x] for x in product if 'image_' in x]
   #       for data in product:
   #          if 'image_' not in data and data != 'id':
   #             response[data] = product[data]
   #       tags = response['tags']
   #       if tags:
   #          response['tags'] = response['tags'].split(', ')
   #       else: 
   #          del response['tags']
   #       if not response['description']:
   #          response['description'] = 'Sin descripción'
   #       response['isfav'] = FavoritesProducts.objects.filter(product=product_result).exists()
   #       return Response(data=response, status=HTTP_200_OK)