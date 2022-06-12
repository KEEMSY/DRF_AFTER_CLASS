from django.contrib import admin

# Register your models here.
from userapp.models import User, UserProfile, Interest

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Interest)