from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/add/', views.CategoriaCreate.as_view(), name='categorias-add'),
    path('subcategorias/',views.SubCategoriaList.as_view(),name='subcategorias-list'),
    path('subcategorias/add',views.SubCategoriaCreate.as_view(),name='subcategorias-add'),
    path('categoria/<pk>/', views.CategoriaDetail.as_view(),name="categoria-detail"),
    path('categoria/update/<pk>',views.CategoriaUpdate.as_view(),name="categoria-update")

]