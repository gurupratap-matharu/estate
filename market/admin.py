from django.contrib import admin

from market.models import Apartment, House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('square_footage', 'num_bedrooms', 'num_bathrooms', 'num_stories', 'garage', 'yard_fenced',)


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('square_footage', 'num_bedrooms', 'num_bathrooms', 'balcony', 'laundry',)


admin.site.register(House, HouseAdmin)
admin.site.register(Apartment, ApartmentAdmin)
