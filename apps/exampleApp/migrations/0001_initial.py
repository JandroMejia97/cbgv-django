# Generated by Django 3.1 on 2020-08-25 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la categoría.', max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorías',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la sub categoría.', max_length=50, verbose_name='nombre')),
                ('categoria', models.ForeignKey(help_text='Categoría principal.', on_delete=django.db.models.deletion.CASCADE, to='exampleApp.categoria', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'SubCategoría',
                'verbose_name_plural': 'SubCategorías',
                'ordering': ('categoria', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del produto.', max_length=50, verbose_name='nombre')),
                ('descripion', models.TextField(help_text='Descripción del producto.', max_length=150, verbose_name='descripcion')),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio del producto.', max_digits=10, verbose_name='precio')),
                ('categoria', models.ForeignKey(help_text='Categoría del producto.', on_delete=django.db.models.deletion.CASCADE, to='exampleApp.subcategoria', verbose_name='categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ('nombre',),
            },
        ),
    ]
