from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/add/', views.CategoriaCreate.as_view(), name='categorias-add'),
    path('categorias/<pk>/', views.CategoriaDetail.as_view(),name="categorias-detail"),
    path('categorias/<pk>/update/',views.CategoriaUpdate.as_view(),name="categorias-update"),
    path('categorias/<pk>/delete/', views.CategoriaDelete.as_view(), name='categorias-delete'),
    path('subcategorias/',views.SubCategoriaList.as_view(),name='subcategorias-list'),
    path('subcategorias/add',views.SubCategoriaCreate.as_view(),name='subcategorias-add'),
    

]