from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    #Para crud de categorias
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/add/', views.CategoriaCreate.as_view(), name='categorias-add'),
    path('categorias/<pk>/', views.CategoriaDetail.as_view(),name="categorias-detail"),
    path('categorias/<pk>/update/',views.CategoriaUpdate.as_view(),name="categorias-update"),
    path('categorias/<pk>/delete/', views.CategoriaDelete.as_view(), name='categorias-delete'),
    #Para crud de SubCategoria
    path('subcategorias/',views.SubCategoriaList.as_view(),name='subcategorias-list'),
    path('subcategorias/add',views.SubCategoriaCreate2.as_view(),name='subcategorias-add'),
    path('subcategoria/<pk>',views.SubCategoriaDetail.as_view(),name="subcategorias-detail"),
    path('subcategorias/<pk>/delete/', views.SubCategoriaDelete.as_view(), name='subcategorias-delete'),
    path('subcategorias/<pk>/update/',views.SubCategoriaUpdate.as_view(),name="subcategorias-update"),
    #Para el crud de productos
    path('productos/',views.ProductoList.as_view(),name='productos-list'),
    path('productos/add/', views.ProductoCreate.as_view(), name='productos-add'),
    path('productos/<pk>/', views.ProductoDetail.as_view(),name="productos-detail"),
    path('productos/<pk>/update/',views.ProductoUpdate.as_view(),name="productos-update"),
     path('productos/<pk>/delete/', views.ProductoDelete.as_view(), name='productos-delete'),

]