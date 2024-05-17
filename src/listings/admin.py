from django.contrib import admin

# Register your models here.

from listings.models import Band
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('name', 'band')

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)