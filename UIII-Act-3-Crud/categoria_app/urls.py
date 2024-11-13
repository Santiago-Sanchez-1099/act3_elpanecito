from django.urls import path
from  categoria_app import views

urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path('registrarCategoria/',views.registrarCategoria,name='registrarCategoria'),
    path('seleccionarCategoria/<id_categoria>', views.seleccionarCategoria, name='seleccionarCategoria'),
    path('editarCategoria/',views.editarCategoria,name='editarCateoria'),
    path('borrarCategoria/<id_categoria>',views.borrarCategoria,name='borrarCategoria'),
]