from django.shortcuts import render,redirect
from .models import *
import os 
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

def cargarInicio(request):
    producto1 = Producto.objects.get(sku = 1)
    producto2 = Producto.objects.get(sku = 2)
    producto3 = Producto.objects.get(sku = 3)
    return render(request, "inicio.html",{"prod1":producto1,"prod2":producto2,"prod3":producto3})

def cargarCompras(request):
    productos = Producto.objects.all()
    return render(request, "compras.html",{"prod":productos})

def cargarRegistrar(request):
    return render(request, "registrar.html")

def cargarIniciarSesion(request):
    return render(request, "iniciarSesion.html")

def cargarAgregar(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,"agregar.html",{"cate":categorias, "prod":productos})

def agregarProducto(request):
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_image = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku, nombre= v_nombre, descripcion = v_descripcion, stock = v_stock,precio = v_precio,fecha_vencimiento = v_fecha_vencimiento, image_url = v_image, categoria_id = v_categoria )

    return redirect('/agregar')

def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()

    cateId = productos.categoria_id

    productoCategoria = Categoria.objects.get(categoria_id = cateId.categoria_id).categoria_id

    return render(request,"editar.html",{"prod":productos, "cate":categorias,"categoriaId":productoCategoria})

def editarProductoForm(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])


    try:
        v_image = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.image_url))
        os.remove(ruta_imagen)
    except:
        v_image = productoBD.image_url


    productoBD.nombre = v_nombre
    productoBD.descripcion = v_descripcion
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.fecha_vencimiento = v_fecha_vencimiento
    productoBD.image_url = v_image
    productoBD.categoria_id = v_categoria


    productoBD.save()
    return redirect('/agregar')


def eliminarProducto(request,sku):
    print("ELIMINAR PRODUCTO",sku)
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.image_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregar')









def registrarUsuario(request):
    v_rut = request.POST['txtRut']
    v_nombre = request.POST['txtNombre']
    v_apellido = request.POST['txtApellido']
    v_correo = request.POST['txtCorreo']
    v_contraseña = request.POST['txtContraseña']
    
    Usuario.objects.create(rut = v_rut, nombre= v_nombre, apellido = v_apellido, correo = v_correo, contraseña = v_contraseña)

    return redirect('/registrar')

def cargarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,"usuarios.html",{"usua":usuarios})

def eliminarUsuario(request,rut):
    print("ELIMINAR USUARIO",rut)
    usuario = Usuario.objects.get(rut = rut)
    usuario.delete()
    return redirect('/usuarios')



def cargarEditarUsuario(request,rut):
    usuarios = Usuario.objects.get(rut = rut)

    return render(request,"editarUsuario.html",{"usua":usuarios})


def editarUsuarioForm(request):
    v_rut = request.POST['txtRut']
    usuarioBD = Usuario.objects.get(rut = v_rut)
    v_nombre = request.POST['txtNombre']
    v_apellido = request.POST['txtApellido']
    v_correo = request.POST['txtCorreo']
    


    usuarioBD.nombre = v_nombre
    usuarioBD.apellido = v_apellido
    usuarioBD.correo = v_correo

    usuarioBD.save()
    return redirect('/usuarios')







def cargarSuscripcion(request):
    return render(request,"suscripcion.html")

def cargarTablaSuscripciones(request):
    suscripciones = Suscripcion.objects.all()
    return render(request,"suscripcionesTabla.html",{"sus":suscripciones})

def registrarSuscripcion(request):
    v_rut = request.POST['txtRut']
    v_nombre = request.POST['txtNombre']
    v_apellido = request.POST['txtApellido']
    v_correo = request.POST['txtCorreo']
    
    Suscripcion.objects.create(rut = v_rut, nombre= v_nombre, apellido = v_apellido, correo = v_correo)

    return redirect('/suscripciones')


def eliminarSuscripcion(request,rut):
    print("ELIMINAR SUSCRIPCION",rut)
    suscripcion = Suscripcion.objects.get(rut = rut)
    suscripcion.delete()
    return redirect('/tablaSuscripcion')



def cargarEditarSuscripciones(request,rut):
    suscripcion = Suscripcion.objects.get(rut = rut)

    return render(request,"editarSuscripciones.html",{"sus":suscripcion})


def editarSuscripcionForm(request):
    v_rut = request.POST['txtRut']
    suscripcionBD = Suscripcion.objects.get(rut = v_rut)
    v_nombre = request.POST['txtNombre']
    v_apellido = request.POST['txtApellido']
    v_correo = request.POST['txtCorreo']
    


    suscripcionBD.nombre = v_nombre
    suscripcionBD.apellido = v_apellido
    suscripcionBD.correo = v_correo

    suscripcionBD.save()
    return redirect('/tablaSuscripcion')


def reducir_stock(request, sku):
    producto = Producto.objects.get(sku = sku)
    if producto.stock > 0 :
        producto.stock = producto.stock - 1
        if producto.stock <= 0:
            producto.delete()
        else:
            producto.save()

    return redirect('/compras')

    
