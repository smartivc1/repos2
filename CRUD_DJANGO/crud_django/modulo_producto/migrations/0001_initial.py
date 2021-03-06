# Generated by Django 2.0.2 on 2021-11-03 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('stockInicial', models.PositiveIntegerField(blank=True, verbose_name='Cantidad inicial')),
                ('stockActual', models.PositiveIntegerField(blank=True, verbose_name='Cantidad disponible')),
                ('precio', models.PositiveIntegerField(verbose_name='Precio de Compra')),
                ('estado', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
