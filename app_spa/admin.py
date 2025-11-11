from django.contrib import admin
from .models import Empleados, Clientes, Servicios

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'duracion', 'tipo_servicio', 'total_empleados']
    search_fields = ['nombre', 'tipo_servicio']
    list_filter = ['tipo_servicio']

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cargo', 'servicio', 'telefono']
    list_filter = ['cargo', 'servicio']
    search_fields = ['nombre', 'apellido']

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'telefono', 'fecha_registro']
    list_filter = ['fecha_registro']
    search_fields = ['nombre', 'apellido', 'email']

admin.site.site_header = "Administración SPA"
admin.site.site_title = "Sistema SPA"
admin.site.index_title = "Bienvenido al Sistema de Administración SPA"