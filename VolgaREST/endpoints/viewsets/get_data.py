from django.db.models import query
from rest_framework import response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.decorators import action
from django.forms.models import model_to_dict
from VolgaREST.root.models import (
   UserModel, ProductModel,
   ProductModel, ContactNetworksModel,
   ClientsOpinionsModel, FollowersModel,
   FavoritesProducts)
from random import sample

class GetDataViewSet(GenericViewSet):

   queryset = UserModel.objects.all()
   blankpicture = 'https://res.cloudinary.com/volga/image/upload/v1611089503/blankpp-men.png'

   def format_opinions(self, opinion_instance):
      opinion_dict = model_to_dict(opinion_instance)
      del opinion_dict['id'], opinion_dict['to_user']
      opinion_dict['from'] = opinion_dict.pop('from_user')
      opinion_dict['date'] = opinion_instance.date.strftime('%d/%m/%Y')
      return opinion_dict

   @action(methods=['get'], detail=False)
   def product(self, request):
      params = request.GET
      username, productkey = params['username'], params['productkey']
      result = ProductModel.objects.filter(user=username, key=productkey)
      if not result.exists():
         raise ValidationError({'error': 404})
      else:
         product_result = result.first()
         product = model_to_dict(product_result)
         response = {}
         response['images'] = [product[x] for x in product if 'image_' in x]
         for data in product:
            if 'image_' not in data and data != 'id':
               response[data] = product[data]
         tags = response['tags']
         if tags:
            response['tags'] = response['tags'].split(', ')
         else: 
            del response['tags']
         if not response['description']:
            response['description'] = 'Sin descripción'
         response['isfav'] = FavoritesProducts.objects.filter(product=product_result).exists()
         return Response(data=response, status=HTTP_200_OK)
      
   @action(methods=['get'], detail=False)
   def user(self, request):
      username = request.GET['username']
      if username == 'me':
         token = request.headers['Authorization'][6:] 
         user = UserModel.objects.get(auth_token=token)
      else:
         user = UserModel.objects.get(username=request.GET['username'])
      
      opinions = ClientsOpinionsModel.objects.filter(to_user=user)
      followers = FollowersModel.objects.filter(user=user)
      products = ProductModel.objects.filter(user=user)
      clients_ratings, opinions_data = [], []
      for opinion in opinions:
         opinion_dict = self.format_opinions(opinion)
         clients_ratings.append(opinion_dict['rating'])
         opinions_data.append(opinion_dict)
      
      if len(clients_ratings) < 1:
         clients_ratings = [0]

      products_data = []
      for product in products:
         product_dict = model_to_dict(product)
         product_response = {}
         for data in product_dict:
            if data in ['image_1', 'product', 'price']:
               product_response[data] = product_dict[data]
         products_data.append(product_response)
      
      authtoken = request.headers['Authorization'][6:]
      client = UserModel.objects.get(auth_token=authtoken)
      following = FollowersModel.objects.filter(user=client)
      
      response = {
         'user': {
            'username': user.username,
            'name': user.name,
            'picture': user.picture or self.blankpicture,
            'stats': {
               'rating_avg': round(sum(clients_ratings)/len(clients_ratings), 2),
               'followers': followers.count(),
               'products': products.count()
            },
            'products': products_data,
            'opinions': opinions_data[0:5] if len(opinions_data) > 5 else opinions_data,
            'following': following.exists()
         }
      }

      return Response(data=response, status=HTTP_200_OK)
   
   @action(methods=['get'], detail=False, url_path='clients-opinions')
   def clients_opinions(self, request):
      opinions = ClientsOpinionsModel.objects.filter(to_user=request.GET['username'])
      opinions_data = []
      for opinion in opinions:
         opinions_data.append(self.format_opinions(opinion))
      return Response(data=opinions_data, status=HTTP_200_OK)
      
   @action(methods=['get'], detail=False, url_path='contact-networks')
   def contact_networks(self, request):
      user = ContactNetworksModel.objects.filter(user_id=request.GET['username'])
      if user.exists():
         usercontact = model_to_dict(user.first())
         del usercontact['user']
         return Response(data=usercontact, status=HTTP_200_OK)
      else:
         raise ValidationError({'user': 'Este usuario no ha registrado redes de contacto.'})
      
   @action(methods=['post'], detail=False)
   def search(self, request):
      data = request.data
      query, filter = data['query'], data['filter']
      if query:
         if filter == 'products':
            result = ProductModel.objects.filter(product__icontains=query)
            needed_data = ['image_1', 'product', 'price', 'key']
            if result.exists():
               response = {'data': {'results': []}, 'status': HTTP_200_OK}
               for product in result:
                  product_dict = model_to_dict(product)
                  product_response = {'user': {}}            
                  for data in product_dict:
                     user_info = product_response['user']
                     user_info['picture'] = product.user.picture or self.blankpicture
                     user_info['username'] = product.user.username
                     user_info['name'] = product.user.name               
                     if data in needed_data:
                        product_response[data] = product_dict[data]
                  product_response['isfav'] = FavoritesProducts.objects.filter(product=product).exists()
                  response['data']['results'].append(product_response)
            else:
               response = {'status': HTTP_204_NO_CONTENT}
         else:
            users = UserModel.objects.filter(username__icontains=query)
            response = {'data': {'results': []}, 'status': HTTP_200_OK}
            for user in users:
               user_dict = model_to_dict(user)
               user_data = {}
               for data in user_dict:
                  if data in ['username', 'name', 'picture']:
                     user_data[data] = user_dict[data]
                  city = user_dict['city']
                  country = user_dict['country']
                  user_data['location'] = f'{city}, {country}'.title()
                  # import pdb; pdb.set_trace()
                  user_data['picture'] = user_dict['picture'] or self.blankpicture
               response['data']['results'].append(user_data)
      else:
         response = {'status': HTTP_204_NO_CONTENT}
      return Response(**response)
   
   @action(methods=['post'], detail=False)
   def explore(self, request):
      querytags = request.data['querytags']
      explore_results = ProductModel.objects.filter(tags__contains=querytags)
      response = []
      needed_data = ['image_1', 'product', 'price', 'key']
      for result in explore_results:
         product_dict = model_to_dict(result)
         product_response = {'user': {}}            
         for data in product_dict:
            user_info = product_response['user']
            user_info['picture'] = result.user.picture or self.blankpicture
            user_info['username'] = result.user.username
            user_info['name'] = result.user.name               
            if data in needed_data:
               product_response[data] = product_dict[data]
         product_response['isfav'] = FavoritesProducts.objects.filter(product=result).exists()
         response.append(product_response)
      return Response(data=response, status=HTTP_200_OK)
   
   @action(methods=['get'], detail=False, url_path='favorites-products')
   def favorites_products(self, request):
      user = request.__dict__['_user']
      favs = FavoritesProducts.objects.filter(user=user)
      needed_data = ['image_1', 'product', 'price', 'key']
      response = []
      for fav in favs:
         product_dict = model_to_dict(fav.product)
         product_response = {'user': {}}            
         for data in product_dict:
            user_info = product_response['user']
            user_info['picture'] = fav.user.picture or self.blankpicture
            user_info['username'] = fav.user.username
            user_info['name'] = fav.user.name               
            if data in needed_data:
               product_response[data] = product_dict[data]
         product_response['isfav'] = FavoritesProducts.objects.filter(product=fav.product).exists()
         response.append(product_response)
      return Response(data=response, status=HTTP_200_OK)

   @action(methods=['get'], detail=False)
   def feed(self, request):
      user = request.__dict__['_user']
      following = FollowersModel.objects.filter(follower=user)
      feed_response = []
      for following_user in following:
         user_products = ProductModel.objects.filter(user=following_user.user)
         if len(user_products) != 0:     
            needed_data = ['image_1', 'product', 'price', 'key']       
            for userprod in user_products:
               product_dict = model_to_dict(userprod)
               product_response = {'user': {}}            
               for data in product_dict:
                  user_info = product_response['user']
                  user_info['picture'] = userprod.user.picture or self.blankpicture
                  user_info['username'] = userprod.user.username
                  user_info['name'] = userprod.user.name               
                  if data in needed_data:
                     product_response[data] = product_dict[data]
               product_response['isfav'] = FavoritesProducts.objects.filter(product=userprod.product).exists()               
               feed_response.append(product_response)
      return Response(data=feed_response, status=HTTP_200_OK)
   
   @action(methods=['get'], detail=False, url_path='landing-products', authentication_classes=[], permission_classes=[])
   def landing_products(self, request):
      products = list(ProductModel.objects.all())
      random_prods = sample(products, 3)
      response = []
      needed_data = ['image_1', 'product', 'price', 'key']
      for product in random_prods:
         product_response = {'user': {}}
         product_dict = model_to_dict(product)
         for data in product_dict:
            user_info = product_response['user']
            user_info['picture'] = product.user.picture or self.blankpicture
            user_info['username'] = product.user.username
            user_info['name'] = product.user.name
            if data in needed_data:
               product_response[data] = product_dict[data]
         response.append(product_response)
      return Response(data=response, status=HTTP_200_OK)

   # @action(methods=['get'], detail=False, url_path='profile-picture')
   # def profile_picture(self, request):
   #    picture = request.__dict__['_user'].picture
   #    return Response(data={'picture': picture or self.blankpicture})
