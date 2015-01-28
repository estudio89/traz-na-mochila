from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import *

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline,]

class TripAdmin(admin.ModelAdmin):
    list_display = ('traveler', 'trip_to', 'departure_date', 'return_date', 'info')

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
