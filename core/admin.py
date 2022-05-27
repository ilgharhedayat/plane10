from django.contrib import admin

# Register your models here.
from .models import SiteSetting, AboutUs, ContactUs

admin.site.register(SiteSetting)
admin.site.register(AboutUs)
admin.site.register(ContactUs)
