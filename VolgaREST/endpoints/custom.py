from django.contrib.auth import models, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

class IdentifyUserMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
   def __call__(self, request):
      authorization = request.headers.get('Authorization', None)
      # request.user = models.AnonymousUser
      if authorization:
         token = authorization[6::]
         token_instance = Token.objects.filter(key=token)
         if token_instance.exists():
            # import pdb; pdb.set_trace()
            request._force_auth_user = token_instance.first().user
            
      return self.get_response(request)

class CreateViewSet(GenericViewSet, CreateModelMixin):
   pass