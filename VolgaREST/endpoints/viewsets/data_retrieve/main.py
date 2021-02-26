from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import (
   HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND)
from rest_framework.decorators import action
from VolgaREST.root.models import (
   UserModel, ProductModel, ContactNetworksModel,
   ClientsOpinionsModel, FollowersModel, FavoritesProducts)
from .formatter import ModelFormatter

class GetDataViewSet(GenericViewSet):
   
   queryset = UserModel.objects.all()
   formatter = ModelFormatter()
   http_method_names = ['get']

   @action(detail=False)
   def product(self, request):
      params = request.GET
      username, key = params['username'], params['key']
      result = ProductModel.objects.filter(user=username, key=key)
      response = {'status': HTTP_404_NOT_FOUND}
      if result.exists():
         respdata = self.formatter.product(result.first())
         response = {'data': respdata, 'status': HTTP_200_OK}
      return Response(**response)
   
   @action(detail=False)
   def search(self, request):
      query, filter = request.GET['query'], request.GET['filter']
      if query:
         response = {'data': [], 'status': HTTP_200_OK}
         if filter == 'products':
            products = ProductModel.objects.filter(product__icontains=query)
            if products.exists():
               for product in products:
                  prod_result = self.formatter.product(product, True)
                  response['data'].append(prod_result)
         if filter == 'users':
            users = UserModel.objects.filter(username__icontains=query)
            if users.exists():
               for user in users:
                  user_result = self.formatter.user_presentation(user)
                  user_result['location'] = f'{user.city}, {user.country}'
                  response['data'].append(user_result)
      return Response(**response)

   @action(detail=False, url_path='clients-opinions')
   def clients_opinions(self, request):
      username = request.GET['username']
      opinions = ClientsOpinionsModel.objects.filter(to_user=username)
      response = {'data': [], 'status': HTTP_200_OK}
      if opinions.exists():
         for op in opinions:
            opinion_data = self.formatter.opinion(op)
            response['data'].append(opinion_data)
      return Response(**response)

   @action(detail=False, url_path='contact-networks')
   def contact_networks(self, request):
      username = request.GET['username']
      contact = ContactNetworksModel.objects.filter(user=username)
      response = {'status': HTTP_404_NOT_FOUND}
      if contact.exists():
         user_contact = self.formatter.contact_networks(contact.first())
         user_contact['email'] = 'mailto:{}'.format(user_contact.pop('email'))
         response = {'data': user_contact, 'status': HTTP_200_OK}
      return Response(**response)

   @action(detail=False)
   def explore(self, request):
      querytags = request.GET['querytags']
      explore_results = ProductModel.objects.filter(tags__contains=querytags)
      response = {'status': HTTP_404_NOT_FOUND}
      if explore_results.exists():
         response = {'data': [], 'status': HTTP_200_OK}
         for result in explore_results:
            result_data = self.formatter.product(result, True)
            response['data'].append(result_data)
      return Response(**response)

   @action(detail=False, url_path='favorites-products')
   def favorites_products(self, request):
      user = request.__dict__['_user']
      favs = FavoritesProducts.objects.filter(user=user)
      response = {'status': HTTP_204_NO_CONTENT}
      if favs.exists():
         response = {'data': [], 'status': HTTP_200_OK}
         for fav in favs:
            product = fav.product
            fav_data = self.formatter.product(product, True)
            response['data'].append(fav_data)
      return Response(**response)

   @action(detail=False)
   def feed(self, request):
      me = request.__dict__['_user']
      users_following = FollowersModel.objects.filter(follower=me)
      response = {'status': HTTP_204_NO_CONTENT}
      if users_following.exists():
         response = {'data': [], 'status': HTTP_200_OK}
         for following in users_following:
            user_products = ProductModel.objects.filter(user=following.user)
            for product in user_products:
               product_data = self.formatter.product(product, True)
               response['data'].append(product_data)
      return Response(**response)
         
   @action(detail=False)
   def user(self, request):
      username = request.GET['username']
      query = UserModel.objects.filter(username=username)
      response = {'status': HTTP_404_NOT_FOUND}
      if query.exists():
         user = query.first()
         opinions = ClientsOpinionsModel.objects.filter(to_user=user)
         products = ProductModel.objects.filter(user=user)
         data_instances = {'opinions': opinions, 'products': products}
         user_data = self.formatter.user_profile(data_instances, username)
         fquery = {'user': username, 'follower': request.__dict__['_user']}
         user_data['following'] = FollowersModel.objects.filter(**fquery).exists()
         user_data |= self.formatter.user_presentation(user)
         response = {'data': user_data, 'status': HTTP_200_OK}
      return Response(**response)
