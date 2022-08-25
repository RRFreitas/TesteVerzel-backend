from django.contrib import admin

# Register your models here.

from .models import Module, Class

admin.site.register(Module)
admin.site.register(Class)
