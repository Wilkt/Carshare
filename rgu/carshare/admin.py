from django.contrib import admin
from .models import Newuser, Payment, Driver
# Register your models here.

admin.site.register(Newuser)
admin.site.register(Payment)
admin.site.register(Driver)