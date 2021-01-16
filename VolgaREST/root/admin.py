from django.contrib import admin
from .models import UserModel, ContactNetworksModel, UserTagsModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(ContactNetworksModel)
admin.site.register(UserTagsModel)
