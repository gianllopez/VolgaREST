from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from VolgaREST.endpoints import LogupViewSet, ContactNetworksViewSet, UserTagsViewSet

volgaRouter = DefaultRouter()

volgaRouter.register('api/v1/users/logup', LogupViewSet)
volgaRouter.register('api/v1/users/contact', ContactNetworksViewSet)
volgaRouter.register('api/v1/users/tags', UserTagsViewSet)

urlpatterns = volgaRouter.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-auth-token/', obtain_auth_token)
]
