from django.contrib import admin
from .models import Employe
# Register your models here.

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

admin.site.register(Employe, EmployeAdmin)