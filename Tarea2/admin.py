from django.contrib import admin

# Register your models here.
from .models import Categoria, RazonSocial, Sancionatorios, Fiscalizacion

class RazonSocialInline(admin.TabularInline):
  model = RazonSocial
  extra = 1
  
class CategoriaInline(admin.TabularInline):
  model = Categoria
  extra = 1

class FiscalizacionInline(admin.TabularInline):
  model = Fiscalizacion
  extra = 1

class Sancionatirio(admin.ModelAdmin):
  fieldsets = [
    ('ID', {'fields': ['expediente']}),
    ('Informacion', {'fields': ['region', 'estado', 'link']})
  ]
  inlines = [RazonSocialInline, CategoriaInline, FiscalizacionInline]
  list_display = ('expediente', 'region', 'estado', 'link')
  search_fields = ('expediente', 'region', 'estado', 'link')
  
  
admin.site.register(Sancionatorios, Sancionatirio)
