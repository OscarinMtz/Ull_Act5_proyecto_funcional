from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Empleados, Clientes, Servicios

# ==================== VISTAS GENERALES ====================
def inicio_spa(request):
    servicios = Servicios.objects.all()[:3]
    empleados = Empleados.objects.all()[:3]
    clientes = Clientes.objects.all()[:3]
    
    # Contar totales para las estadísticas
    total_empleados = Empleados.objects.count()
    total_clientes = Clientes.objects.count()
    total_servicios = Servicios.objects.count()
    
    # Obtener todos los servicios con sus empleados para las relaciones
    todos_servicios = Servicios.objects.prefetch_related('empleados').all()
    
    return render(request, 'inicio.html', {
        'servicios': servicios,
        'empleados': empleados,
        'clientes': clientes,
        'empleados_count': total_empleados,
        'clientes_count': total_clientes,
        'servicios_count': total_servicios,
        'todos_servicios': todos_servicios
    })

# ==================== VISTAS EMPLEADOS ====================
def agregar_empleado(request):
    servicios = Servicios.objects.all()
    if request.method == 'POST':
        servicio_id = request.POST['servicio']
        servicio = Servicios.objects.get(id_servicios=servicio_id)
        
        empleado = Empleados(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            especialidad=request.POST['especialidad'],
            telefono=request.POST['telefono'],
            cargo=request.POST['cargo'],
            servicio=servicio
        )
        empleado.save()
        messages.success(request, 'Empleado agregado correctamente!')
        return redirect('ver_empleados')
    return render(request, 'empleados/agregar_empleado.html', {'servicios': servicios})

def ver_empleados(request):
    empleados = Empleados.objects.select_related('servicio').all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    servicios = Servicios.objects.all()
    try:
        empleado = Empleados.objects.get(id_empleados=id)
        if request.method == 'POST':
            servicio_id = request.POST['servicio']
            servicio = Servicios.objects.get(id_servicios=servicio_id)
            
            empleado.nombre = request.POST['nombre']
            empleado.apellido = request.POST['apellido']
            empleado.especialidad = request.POST['especialidad']
            empleado.telefono = request.POST['telefono']
            empleado.cargo = request.POST['cargo']
            empleado.servicio = servicio
            empleado.save()
            messages.success(request, 'Empleado actualizado correctamente!')
            return redirect('ver_empleados')
        return render(request, 'empleados/actualizar_empleado.html', {
            'empleado': empleado,
            'servicios': servicios
        })
    except Empleados.DoesNotExist:
        messages.error(request, 'El empleado no existe.')
        return redirect('ver_empleados')

def borrar_empleado(request, id):
    try:
        empleado = Empleados.objects.get(id_empleados=id)
        if request.method == 'POST':
            empleado.delete()
            messages.success(request, 'Empleado eliminado correctamente!')
            return redirect('ver_empleados')
        return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})
    except Empleados.DoesNotExist:
        messages.error(request, 'El empleado no existe.')
        return redirect('ver_empleados')

# ==================== VISTAS CLIENTES ====================
def agregar_cliente(request):
    if request.method == 'POST':
        cliente = Clientes(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
            alergias=request.POST.get('alergias', ''),
            preferencias=request.POST.get('preferencias', '')
        )
        cliente.save()
        messages.success(request, 'Cliente agregado correctamente!')
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_cliente.html')

def ver_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    try:
        cliente = Clientes.objects.get(id_clientes=id)
        if request.method == 'POST':
            cliente.nombre = request.POST['nombre']
            cliente.apellido = request.POST['apellido']
            cliente.email = request.POST['email']
            cliente.telefono = request.POST['telefono']
            cliente.alergias = request.POST.get('alergias', '')
            cliente.preferencias = request.POST.get('preferencias', '')
            cliente.save()
            messages.success(request, 'Cliente actualizado correctamente!')
            return redirect('ver_clientes')
        return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})
    except Clientes.DoesNotExist:
        messages.error(request, 'El cliente no existe.')
        return redirect('ver_clientes')

def borrar_cliente(request, id):
    try:
        cliente = Clientes.objects.get(id_clientes=id)
        if request.method == 'POST':
            cliente.delete()
            messages.success(request, 'Cliente eliminado correctamente!')
            return redirect('ver_clientes')
        return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})
    except Clientes.DoesNotExist:
        messages.error(request, 'El cliente no existe.')
        return redirect('ver_clientes')

# ==================== VISTAS SERVICIOS ====================
def agregar_servicio(request):
    if request.method == 'POST':
        servicio = Servicios(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            duracion=request.POST['duracion'],
            tipo_servicio=request.POST['tipo_servicio']
        )
        if 'imagen' in request.FILES:
            servicio.imagen = request.FILES['imagen']
        servicio.save()
        messages.success(request, 'Servicio agregado correctamente!')
        return redirect('ver_servicios')
    return render(request, 'servicios/agregar_servicio.html')

def ver_servicios(request):
    servicios = Servicios.objects.prefetch_related('empleados').all()
    return render(request, 'servicios/ver_servicios.html', {'servicios': servicios})

def actualizar_servicio(request, id):
    try:
        servicio = Servicios.objects.get(id_servicios=id)
        if request.method == 'POST':
            servicio.nombre = request.POST['nombre']
            servicio.descripcion = request.POST['descripcion']
            servicio.precio = request.POST['precio']
            servicio.duracion = request.POST['duracion']
            servicio.tipo_servicio = request.POST['tipo_servicio']
            if 'imagen' in request.FILES:
                servicio.imagen = request.FILES['imagen']
            servicio.save()
            messages.success(request, 'Servicio actualizado correctamente!')
            return redirect('ver_servicios')
        return render(request, 'servicios/actualizar_servicio.html', {'servicio': servicio})
    except Servicios.DoesNotExist:
        messages.error(request, 'El servicio no existe.')
        return redirect('ver_servicios')

def borrar_servicio(request, id):
    try:
        servicio = Servicios.objects.get(id_servicios=id)
        if request.method == 'POST':
            servicio.delete()
            messages.success(request, 'Servicio eliminado correctamente!')
            return redirect('ver_servicios')
        return render(request, 'servicios/borrar_servicio.html', {'servicio': servicio})
    except Servicios.DoesNotExist:
        messages.error(request, 'El servicio no existe.')
        return redirect('ver_servicios')