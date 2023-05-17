from django.contrib import admin

# Register your models here.
from .models import Station, Location, PaymentType, PaymentStation, StationState

class StationStateInline(admin.TabularInline):
  model = StationState
  max_num = 1
  
class LocationInline(admin.TabularInline):
  model = Location
  max_num = 1
  
class PaymentStationInline(admin.TabularInline):
  model = PaymentStation
  max_num = 4

class StationAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, { 'fields': ['id']}),
    ('Station information', { 'fields': ['uid', 'name', 'slots', 'payment_terminal', 'has_ebike']}),
  ]
  list_display = ('uid','name', 'slots', 'payment_terminal', 'has_ebike')
  list_filter = ['payment_terminal']
  search_fields = ['name']
  inlines = [StationStateInline, LocationInline, PaymentStationInline]
  
class StationStateAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, { 'fields': ['id_station']}),
    ('Station state', { 'fields': ['empty_slots', 'normal_bikes', 'electric_bikes', 'renting', 'returning', 'last_update']}),
  ]
  list_display = ('id_station', 'empty_slots', 'normal_bikes', 'electric_bikes', 'renting', 'returning', 'last_update', 'has_disabled_bikes') 
  list_filter = ['last_update']
  search_fields = ['id_station']
  
class LocationAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, { 'fields': ['id_station']}),
    ('Location', { 'fields': ['latitude', 'longitude', 'altitude', 'address', 'city', 'country']}),
  ]
  list_display = ('id_station', 'latitude', 'longitude', 'altitude', 'address', 'city', 'country')
  list_filter = ['city']
  search_fields = ['id_station']
  
class PaymentTypeAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, { 'fields': ['id']}),
    ('Payment type', { 'fields': ['name']}),
  ]
  ordering = ['id']
  list_display = ('id', 'name')
  
  
admin.site.register(Station, StationAdmin)
admin.site.register(StationState, StationStateAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)