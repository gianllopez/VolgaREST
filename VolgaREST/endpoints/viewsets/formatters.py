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
      return self.fields_filter (
            instance=user_instance,
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
         product_response['tags'] = tags.split(', ')
      if include_user:
         product_response['user'] = self.user(product_instance.user)
      return product_response

   def clients_opinions(self, opinion_instance):
      opdata = self.fields_filter(opinion_instance, ['id', 'to_user'], True)
      opdata['date'] = opinion_instance.date.strftime('%d/%m/%Y')
      opdata['from'] = opdata.pop('from_user')
      return opdata
   
   def contact_networks(self, cn_instance):
      return self.fields_filter(cn_instance, ['user'], True)