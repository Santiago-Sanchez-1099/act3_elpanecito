from django.shortcuts import render, redirect
from .models import Categoria
# Create your views here.

def inicio_vista(request):
    lascategorias=Categoria.objects.all()
    return render(request, 'gestionarCategoria.html',{'miscategorias':lascategorias})

def registrarCategoria(request):
    id_categoria = request.POST["num_id_categoria"]
    nombre_categoria = request.POST["txt_nombre_categoria"]
    descripcion = request.POST["txt_descripcion"]
    estado = request.POST["txt_estado"]
    tipo = request.POST["txt_tipo"]
    fecha_creacion = request.POST["date_fecha_creacion"]
    id_usuario = request.POST["num_id_usuario"]

    guardarcategoria = Categoria.objects.create(id_categoria=id_categoria,nombre_categoria=nombre_categoria,
    descripcion=descripcion,estado=estado,tipo=tipo,fecha_creacion=fecha_creacion,id_usuario=id_usuario)
    return redirect('/')

def seleccionarCategoria(request, id_categoria):
    categoria=Categoria.objects.get(id_categoria=id_categoria)
    return render(request, "editarCategoria.html",{"miscategorias":categoria})

def editarCategoria(request):
    id_categoria = request.POST["num_id_categoria"]
    nombre_categoria = request.POST["txt_nombre_categoria"]
    descripcion = request.POST["txt_descripcion"]
    estado = request.POST["txt_estado"]
    tipo = request.POST["txt_tipo"]
    fecha_creacion = request.POST["date_fecha_creacion"]
    id_usuario = request.POST["num_id_usuario"]
    categoria=Categoria.objects.get(id_categoria=id_categoria)
    categoria.nombre_categoria=nombre_categoria
    categoria.descripcion=descripcion
    categoria.estado=estado
    categoria.tipo=tipo
    categoria.fecha_creacion=fecha_creacion
    categoria.id_usuario=id_usuario
    categoria.save()
    return redirect('/')

def borrarCategoria(request, id_categoria):
    categoria=Categoria.objects.get(id_categoria=id_categoria)
    categoria.delete()
    return redirect("/")