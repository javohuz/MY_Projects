from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationfrom , CustomUserChangefrom
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationfrom
    form = CustomUserChangefrom
    model = CustomUser
    list_display = ['username' , 'number']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('number',)}),

    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('number',)}),

    )

admin.site.register(CustomUser, CustomUserAdmin)