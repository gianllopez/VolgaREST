from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from VolgaREST.endpoints import LogupViewSet

volgaRouter = DefaultRouter()

volgaRouter.register('api/v1/users/logup', LogupViewSet)

urlpatterns = volgaRouter.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
