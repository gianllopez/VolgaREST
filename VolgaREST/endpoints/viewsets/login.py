from rest_framework.viewsets import ViewSet
from ..serializers import LoginSerializer
from VolgaREST.root.models import UserModel

class LoginViewSet(ViewSet):
   
   serializer_class = LoginSerializer
   queryset = UserModel.objects.all()
   authentication_classes = permission_classes = []

   def create(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)