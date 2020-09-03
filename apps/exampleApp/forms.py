from django import forms

from . import models


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = models.Categoria
        fields = ('nombre',)

CategoriaForm2 = forms.modelform_factory(
    model=models.Categoria,
    fields=('nombre',)
)
CategoriaFormset = forms.formset_factory(
    form=CategoriaForm2,
    extra=4,
    min_num=3,
    max_num=6
)

SubCategoriaFormset = forms.inlineformset_factory(
    parent_model=models.Categoria,
    model=models.SubCategoria,
    fields='__all__',
    extra=1,
    min_num=3,
    max_num=8,
)

ProductoFormset = forms.inlineformset_factory(
    parent_model=models.SubCategoria,
    model=models.Producto,
    fields='__all__',
    extra=1,
    min_num=2,
    max_num=8,
)
