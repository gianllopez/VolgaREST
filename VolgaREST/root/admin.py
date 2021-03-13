from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

admin.site.register(UserModel)
admin.site.register(ProductModel)
admin.site.register(FollowersModel)
admin.site.register(FavoritesProducts)
admin.site.register(ContactNetworksModel)
admin.site.register(ClientsOpinionsModel)
