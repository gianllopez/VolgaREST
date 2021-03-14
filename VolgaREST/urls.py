from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from VolgaREST.endpoints import (
    LogupViewSet, ContactNetworksViewSet, UserProfilePictureViewSet,
    ClientOpinionsViewSet, LoginViewSet, ProductsViewSet,
    GetDataViewSet, ValidationViewSet, FollowersViewSet,
    FavoritesProductsViewSet)

volgaRouter = DefaultRouter()

volgaRouter.register('api/v1/logup', LogupViewSet)
volgaRouter.register('api/v1/contact', ContactNetworksViewSet)
volgaRouter.register('api/v1/profile-picture', UserProfilePictureViewSet)
volgaRouter.register('api/v1/opinions', ClientOpinionsViewSet)
volgaRouter.register('api/v1/login', LoginViewSet)
volgaRouter.register('api/v1/products', ProductsViewSet)
volgaRouter.register('api/v1/get-data', GetDataViewSet)
volgaRouter.register('api/v1/validation', ValidationViewSet)
volgaRouter.register('api/v1/follow', FollowersViewSet)
volgaRouter.register('api/v1/product-fav', FavoritesProductsViewSet)

urlpatterns = volgaRouter.urls

urlpatterns += [ path('admin/', admin.site.urls) ]

def not_found(request, exception):
   return HttpResponse('''
      <h1>Page not found</h1>
      <h4>You are a dumb and...</h4>
      <h3>I AM SMARTER THAN YOU.</h3>
      <p>Have a good day :)</p>''')

handler404 = not_found
