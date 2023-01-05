from django.contrib import admin
from .models import *

class bukuadmin (admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'wpp', 'provinsi', 'golongan']

admin.site.register(Lokasi, bukuadmin)
admin.site.register(Location)




