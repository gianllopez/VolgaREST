from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

volgaRouter = DefaultRouter()

urlpatterns = volgaRouter.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
