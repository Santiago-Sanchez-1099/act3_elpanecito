from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def inicio_vista(request):
    lasproductos=Producto.objects.all()
    return render(request, 'gestionarProducto.html',{'misproductos':lasproductos})

def registrarProducto(request):
    id_producto = request.POST["num_id_producto"]
    nombre_producto = request.POST["txt_nombre_producto"]
    descripcion = request.POST["txt_descripcion"]
    stock = request.POST["num_stock"]
    precio = request.POST["num_precio"]
    fecha_ingreso = request.POST["date_fecha_ingreso"]
    id_categoria = request.POST["num_id_categoria"]

    guardarproducto = Producto.objects.create(id_producto=id_producto,nombre_producto=nombre_producto,
    descripcion=descripcion,stock=stock,precio=precio,fecha_ingreso=fecha_ingreso,id_categoria=id_categoria)
    return redirect('/')

def seleccionarProducto(request, id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html",{"misproductos":producto})

def editarProducto(request):
    id_producto = request.POST["num_id_producto"]
    nombre_producto = request.POST["txt_nombre_producto"]
    descripcion = request.POST["txt_descripcion"]
    stock = request.POST["num_stock"]
    precio = request.POST["num_precio"]
    fecha_ingreso = request.POST["date_fecha_ingreso"]
    id_categoria = request.POST["num_id_categoria"]
    producto=Producto.objects.get(id_producto=id_producto)
    producto.nombre_producto=nombre_producto
    producto.descripcion=descripcion
    producto.stock=stock
    producto.precio=precio
    producto.fecha_ingreso=fecha_ingreso
    producto.id_categoria=id_categoria
    producto.save()
    return redirect('/')

def borrarProducto(request, id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("/")