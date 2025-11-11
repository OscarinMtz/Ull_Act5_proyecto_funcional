from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Página principal
    path('', views.inicio_spa, name='inicio_spa'),
    
    # URLs para Empleados
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # URLs para Clientes
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Servicios
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/', views.ver_servicios, name='ver_servicios'),
    path('servicios/actualizar/<int:id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/borrar/<int:id>/', views.borrar_servicio, name='borrar_servicio'),
]

# Para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)