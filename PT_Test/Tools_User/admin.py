from django.contrib import admin
from Tools_User.models import *
# Register your models here.
@admin.register(User)
class admin_user(admin.ModelAdmin):
    list_display = ("user","pwd")