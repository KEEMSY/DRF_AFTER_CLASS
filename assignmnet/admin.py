from django.contrib import admin

# Register your models here.
from assignmnet.models import Enterprise, Place, EnterpriseProfile

admin.site.register(Enterprise)
admin.site.register(EnterpriseProfile)
admin.site.register(Place)