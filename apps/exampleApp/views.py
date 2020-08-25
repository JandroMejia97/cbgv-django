from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *

class SubCategoriaList(generic.ListView):
    model = SubCategoria
    context_object_name= 'subcategorias'


class SubCategoriaCreate(generic.CreateView):
    model = SubCategoria
    fields = '__all__'
    slug_field = 'nombre'
    success_url = reverse_lazy('example:subcategorias-list')


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

class CategoriaList(generic.ListView):
    model = Categoria
    context_object_name = 'categorias'


class CategoriaCreate(generic.CreateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('example:categorias-list')


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name ='./index.html'