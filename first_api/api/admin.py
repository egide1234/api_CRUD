from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
admin.site.register(User, UserAdmin)
