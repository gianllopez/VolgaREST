from VolgaREST.root.models import FollowersModel, FavoritesProducts
from django.forms import model_to_dict

class ModelFormatter:

   @staticmethod
   def blank_picture(gender):
      urlbase = 'https://res.cloudinary.com/volga/image/upload/v1611089503/'
      picture = {
         'masculino': urlbase + 'blankpp-men.png',
         'femenino': urlbase + 'blankpp-women.png',
         'no definido': urlbase + 'blankpp-undefined.png'}
      return picture[gender.lower()]

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
   
   def prodisfav(self, key):
      isfav = FavoritesProducts.objects.filter(product=key)
      return isfav.exists()

   def user_presentation(self, user_instance):
      user_data = self.fields_filter(user_instance, ['username', 'name', 'picture'])
      if not user_data['picture']:
         user_data['picture'] = self.blank_picture(user_instance.gender)
      return user_data
   
   def product(self, product_instance, include_user=False):
      product_data = self.fields_filter(product_instance, ['user'], True)
      product_data['images'] = product_data.pop('images').split(', ')
      product_data['isfav'] = self.prodisfav(product_instance.key)
      if tags := product_data.get('tags', None):
         product_data['tags'] = tags.split(', ')
      if include_user:
         product_data['user'] = self.user_presentation(product_instance.user)
      return product_data

   def opinion(self, opinion_instance):
      opdata = self.fields_filter(opinion_instance, ['id', 'to_user'], True)
      opdata['date'] = opinion_instance.date.strftime('%d/%m/%Y')
      opdata['from'] = opdata.pop('from_user')
      return opdata
   
   def contact_networks(self, cn_instance):
      return self.fields_filter(cn_instance, ['user'], True)
   
   def user_profile(self, instances, username):
      user_data = {}
      ratingavg = []
      for instance in instances:
         queryset = instances[instance]
         data_collection = []
         for data in queryset:
            method = getattr(self, instance[0:-1])
            instance_data = method(data)
            data_collection.append(instance_data)
            rating = instance_data.get('rating', None)
            if rating:
               ratingavg.append(rating)
         user_data[instance] = data_collection
      opinions = user_data['opinions']
      user_data['opinions'] = opinions[0:5] if len(opinions) > 5 else opinions
      n_followers = FollowersModel.objects.filter(user=username).count()  
      ratinglength = len(ratingavg)
      user_data['stats'] = {
         'rating_avg': round((sum(ratingavg) / ratinglength) if ratinglength != 0 else 0, 2),
         'followers': n_followers,
         'total_products': len(instances['products'])}
      return user_data