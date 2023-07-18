from django.contrib import admin

from .models import AccountUser, Adress, Studentprofile

# Register your models here.

admin.site.register(AccountUser)
admin.site.register(Studentprofile)
admin.site.register(Adress)
