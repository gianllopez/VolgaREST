from django.contrib import admin
from .models import UserModel, ContactModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(ContactModel)
