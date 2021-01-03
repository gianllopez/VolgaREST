from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from VolgaREST.api import LogupViewSet

volgaRouter = DefaultRouter()

volgaRouter.register('logup', LogupViewSet)

urlpatterns = volgaRouter.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
