from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarInicio),
    path('iniciarSesion',views.cargarIniciarSesion),
    path('compras',views.cargarCompras),

    path('agregar',views.cargarAgregar),
    path('agregarProductoForm',views.agregarProducto),

    path('editarProducto/<sku>',views.cargarEditarProducto), 
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('editarProductoForm',views.editarProductoForm),
    
    path('registrar',views.cargarRegistrar),
    path('registrarUsuario', views.registrarUsuario),

    path('usuarios',views.cargarUsuarios),
    path('eliminarUsuario/<rut>',views.eliminarUsuario),
    path('editarUsuario/<rut>',views.cargarEditarUsuario),
    path('editarUsuarioForm',views.editarUsuarioForm),

    path('suscripciones',views.cargarSuscripcion),
    path('registrarSuscripcion',views.registrarSuscripcion),
    path('tablaSuscripcion',views.cargarTablaSuscripciones),
    path('eliminarSuscripcion/<rut>',views.eliminarSuscripcion),
    path('editarSuscripcion/<rut>',views.cargarEditarSuscripciones),
    path('editarSuscripcionForm',views.editarSuscripcionForm),

    path('reducir_stock/<sku>',views.reducir_stock)



]
