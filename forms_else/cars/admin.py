from django.contrib import admin

# Register your models here.
# from .models import Cars
from .models import Auto, Make

# admin.site.register(Cars)
admin.site.register(Auto)
admin.site.register(Make)
