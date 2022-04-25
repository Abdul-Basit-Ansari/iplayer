from django.contrib import admin
from .models import Mvideo,Maudio,Vcomment,Acomment
# Register your models here.
admin.site.register((Mvideo,Maudio,Vcomment,Acomment))