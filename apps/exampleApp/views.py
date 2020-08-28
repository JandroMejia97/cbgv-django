from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
#Crud de SubCategorias
class SubCategoriaList(generic.ListView):
    model = SubCategoria
    context_object_name= 'subcategorias'


class SubCategoriaCreate(generic.CreateView):
    model = SubCategoria
    fields = '__all__'
    slug_field = 'nombre'
    success_url = reverse_lazy('example:subcategorias-list')


class SubCategoriaDetail(generic.DetailView):
    model = SubCategoria
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['productos'] = Producto.objects.filter(subcategoria=self.object)
        print(context)
        return context


class SubCategoriaDelete(generic.DeleteView):
    model = SubCategoria
    success_url = reverse_lazy('example:subcategorias-list')


class SubCategoriaUpdate(generic.UpdateView):
    model = SubCategoria
    fields = ['categoria','nombre']
    success_url = reverse_lazy('example:subcategorias-list')


#Crud de Categorias
class CategoriaDetail(generic.DetailView):
    context_object_name = 'categoria'
    model = Categoria

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if self.object:
            context['subcategorias'] = SubCategoria.objects.filter(categoria=self.object)      
        return context


class CategoriaUpdate(generic.UpdateView):
    model = Categoria
    fields = ['nombre']
    success_url = reverse_lazy('example:categorias-list')


class CategoriaDelete(generic.DeleteView):
    model = Categoria
    success_url = reverse_lazy('example:categorias-list')


class CategoriaList(generic.ListView):
    model = Categoria
    context_object_name = 'categorias'


class CategoriaCreate(generic.CreateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('example:categorias-list')


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name ='./index.html'


#Crud para productos
class ProductoList(generic.ListView):
    model = Producto


class ProductoCreate(generic.CreateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('example:productos-list')


class ProductoDetail(generic.DetailView):    
    model = Producto


class ProductoUpdate(generic.UpdateView):
    model = Producto
    fields = ['subcategoria','nombre','descripion','precio']
    success_url = reverse_lazy('example:productos-list')


class ProductoDelete(generic.DeleteView):
    model = Producto
    success_url = reverse_lazy('example:productos-list')