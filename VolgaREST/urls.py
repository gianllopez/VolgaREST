from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from VolgaREST.endpoints import (
    LogupViewSet, ContactNetworksViewSet,
    UserTagsViewSet, UserProfilePictureViewSet,
    ClientOpinionsViewSet, LoginViewSet, NewProductViewSet
)

volgaRouter = DefaultRouter()
apibase = 'api/v1/users'

volgaRouter.register(apibase + '/logup', LogupViewSet)
volgaRouter.register(apibase + '/contact', ContactNetworksViewSet)
volgaRouter.register(apibase + '/tags', UserTagsViewSet)
volgaRouter.register(apibase + '/profile-picture', UserProfilePictureViewSet)
volgaRouter.register(apibase + '/opinions', ClientOpinionsViewSet)
volgaRouter.register(apibase + '/login', LoginViewSet)
volgaRouter.register(apibase + '/products/new', NewProductViewSet)

urlpatterns = volgaRouter.urls

urlpatterns += [
    path('admin/', admin.site.urls)
]
