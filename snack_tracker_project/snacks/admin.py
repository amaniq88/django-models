from django.contrib import admin
from .models import Snack

# class adminSnack(admin.ModelAdmin):
#     pass

admin.site.register(Snack)