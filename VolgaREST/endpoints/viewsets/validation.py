from rest_framework.viewsets import GenericViewSet
from VolgaREST.root.models import UserModel
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from random import randint

class ValidationViewSet(GenericViewSet):
   
   queryset = UserModel.objects.all()

   @action(methods=['post'], detail=False, url_path='user-exists',
           authentication_classes=[], permission_classes=[])
   def user_exists(self, request):
      username = request.data.get('username', None)
      response = {'status': HTTP_404_NOT_FOUND}
      if username:
         user = UserModel.objects.filter(username=username)
         if user.exists():
            response['status'] = HTTP_200_OK
      return Response(**response)
   
   @action(methods=['post'], detail=False, url_path='email-verification')
   def email_verification(self, request):
      user = request.user
      if not user.verified_email and not user.email_code:
         email = request.data['email']
         code = ''
         for x in range(6):
            code += str(randint(50000, 1000000))
         code = code[:6]
         req_config = {
            'subject': 'CÓDIGO DE VERIFICACIÓN - VOLGA',
            'message': f'Tu código de verificación es: {code}',
            'recipient_list': [email],
            'from_email': settings.EMAIL_HOST_USER}
         sent = send_mail(**req_config)
         if sent:
            user.email_code = code
            user.save()
      return Response(status=HTTP_200_OK)
   
   @action(methods=['post'], detail=False, url_path='digits-verification')
   def digits_verification(self, request):
      digits = int(''.join(request.data))
      user = request.user
      response = {'status': HTTP_400_BAD_REQUEST}
      if (user.email_code == digits):
         user.verified_email = True
         user.save()
         response = {'status': HTTP_200_OK}
      return Response(**response)
