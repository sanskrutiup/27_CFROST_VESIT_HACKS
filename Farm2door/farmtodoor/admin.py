from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from farmtodoor.models import Reg, AddProd

admin.site.register(Reg)
admin.site.register(AddProd)