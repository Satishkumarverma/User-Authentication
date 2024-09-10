from django.contrib import admin
from .models import CustomerUser

@admin.register(CustomerUser)
class CustomerUserAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
