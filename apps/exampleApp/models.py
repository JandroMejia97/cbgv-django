from django.db import models
from django.utils.translation import ugettext_lazy as _


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name=_('nombre'),
        help_text=_('Nombre de la categoría.')
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorías')
        ordering = ('nombre',)


class SubCategoria(models.Model):
    categoria = models.ForeignKey(
        blank=False,
        null=False,
        to=Categoria,
        on_delete=models.CASCADE,
        verbose_name=_('categoria'),
        help_text=_('Categoría principal.')
    )
    nombre = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name=_('nombre'),
        help_text=_('Nombre de la sub categoría.')
    )

    def __str__(self):
        return '%s - %s' % (self.categoria, self.nombre)

    class Meta:
        verbose_name = _('SubCategoría')
        verbose_name_plural = _('SubCategorías')
        ordering = ('categoria', 'nombre')


class Producto(models.Model):
    subcategoria = models.ForeignKey(
        blank=False,
        null=False,
        to=SubCategoria,
        on_delete=models.CASCADE,
        verbose_name=_('subcategoría'),
        help_text=_('SubCategoría del producto.')
    )
    nombre = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name=_('nombre'),
        help_text=_('Nombre del produto.')
    )
    descripion = models.TextField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_('descripcion'),
        help_text=_('Descripción del producto.')
    )
    precio = models.DecimalField(
        blank=False,
        null=False,
        max_digits=10,
        decimal_places=2,
        verbose_name=_('precio'),
        help_text=_('Precio del producto.')
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')
        ordering = ('nombre',)
